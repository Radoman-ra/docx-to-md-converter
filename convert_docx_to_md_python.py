#!/usr/bin/env python3
"""
Альтернативный скрипт для конвертации DOCX в Markdown (Pure Python)
Использует python-docx для работы без pandoc

Использование:
    python convert_docx_to_md_python.py [файл.docx]

Требования:
    pip install python-docx
"""

import os
import sys
from pathlib import Path
import zipfile
import shutil

def check_dependencies():
    """Проверка необходимых библиотек"""
    try:
        import docx
        return True
    except ImportError:
        return False

def install_instructions():
    """Инструкции по установке зависимостей"""
    print("\n" + "="*60)
    print("ТРЕБУЕТСЯ УСТАНОВКА БИБЛИОТЕКИ")
    print("="*60)
    print("\nУстановите python-docx:")
    print("  pip install python-docx")
    print("\nИли используйте альтернативный скрипт с pandoc:")
    print("  python convert_docx_to_md.py")
    print("="*60 + "\n")

def extract_images(docx_path, images_dir):
    """Извлечение изображений из .docx файла"""
    images_path = Path(images_dir)
    images_path.mkdir(exist_ok=True)
    
    image_files = []
    
    try:
        with zipfile.ZipFile(docx_path, 'r') as zip_ref:
            # Ищем изображения в архиве
            for file_info in zip_ref.filelist:
                if file_info.filename.startswith('word/media/'):
                    # Извлекаем имя файла
                    image_name = os.path.basename(file_info.filename)
                    
                    # Извлекаем изображение
                    source = zip_ref.open(file_info)
                    target_path = images_path / image_name
                    
                    with open(target_path, 'wb') as target:
                        shutil.copyfileobj(source, target)
                    
                    image_files.append(image_name)
                    
        return image_files
    except Exception as e:
        print(f"⚠ Предупреждение: Не удалось извлечь изображения: {e}")
        return []

def convert_paragraph_to_markdown(paragraph):
    """Конвертация параграфа в markdown"""
    text = paragraph.text.strip()
    
    if not text:
        return ""
    
    # Обработка заголовков (упрощенная логика)
    style = paragraph.style.name.lower()
    
    if 'heading 1' in style or 'заголовок 1' in style:
        return f"# {text}\n"
    elif 'heading 2' in style or 'заголовок 2' in style:
        return f"## {text}\n"
    elif 'heading 3' in style or 'заголовок 3' in style:
        return f"### {text}\n"
    elif 'heading 4' in style or 'заголовок 4' in style:
        return f"#### {text}\n"
    elif 'heading 5' in style or 'заголовок 5' in style:
        return f"##### {text}\n"
    elif 'heading 6' in style or 'заголовок 6' in style:
        return f"###### {text}\n"
    
    # Обработка форматирования текста
    result = ""
    for run in paragraph.runs:
        run_text = run.text
        
        # Жирный текст
        if run.bold:
            run_text = f"**{run_text}**"
        
        # Курсив
        if run.italic:
            run_text = f"*{run_text}*"
        
        result += run_text
    
    return result + "\n"

def convert_table_to_markdown(table):
    """Конвертация таблицы в markdown"""
    if not table.rows:
        return ""
    
    md_table = []
    
    # Заголовок таблицы
    header_cells = [cell.text.strip() for cell in table.rows[0].cells]
    md_table.append("| " + " | ".join(header_cells) + " |")
    md_table.append("| " + " | ".join(["---"] * len(header_cells)) + " |")
    
    # Остальные строки
    for row in table.rows[1:]:
        cells = [cell.text.strip() for cell in row.cells]
        md_table.append("| " + " | ".join(cells) + " |")
    
    return "\n".join(md_table) + "\n"

def convert_docx_to_markdown(docx_path, output_path, images_dir):
    """Основная функция конвертации"""
    from docx import Document
    from docx.oxml.text.paragraph import CT_P
    from docx.oxml.table import CT_Tbl
    from docx.table import _Cell, Table
    from docx.text.paragraph import Paragraph
    
    # Загружаем документ
    doc = Document(docx_path)
    
    # Извлекаем изображения
    print("Извлечение изображений...")
    image_files = extract_images(docx_path, images_dir)
    
    markdown_content = []
    image_index = 0
    
    print("Конвертация содержимого...")
    
    # Проходим по всем элементам документа
    for element in doc.element.body:
        if isinstance(element, CT_P):
            # Это параграф
            paragraph = Paragraph(element, doc)
            
            # Проверяем на изображения в параграфе
            if paragraph._element.xpath('.//pic:pic'):
                if image_index < len(image_files):
                    image_path = f"{images_dir}/{image_files[image_index]}"
                    markdown_content.append(f"\n![Image]({image_path})\n")
                    image_index += 1
            
            md_text = convert_paragraph_to_markdown(paragraph)
            if md_text:
                markdown_content.append(md_text)
                
        elif isinstance(element, CT_Tbl):
            # Это таблица
            table = Table(element, doc)
            md_table = convert_table_to_markdown(table)
            if md_table:
                markdown_content.append("\n" + md_table + "\n")
    
    # Сохраняем результат
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(markdown_content))
    
    return len(image_files)

def main():
    # Проверяем зависимости
    if not check_dependencies():
        install_instructions()
        sys.exit(1)
    
    # Проверяем аргументы командной строки
    if len(sys.argv) > 1:
        docx_file = sys.argv[1]
    else:
        # Ищем .docx файлы в текущей директории
        docx_files = list(Path('.').glob('*.docx'))
        if not docx_files:
            print("❌ Ошибка: Файлы .docx не найдены!")
            print("\nИспользование:")
            print("  python convert_docx_to_md_python.py <файл.docx>")
            print("  или просто запустите скрипт в папке с .docx файлом")
            sys.exit(1)
        
        if len(docx_files) > 1:
            print("Найдено несколько .docx файлов:")
            for i, f in enumerate(docx_files, 1):
                print(f"  {i}. {f}")
            print("\nУкажите файл явно:")
            print("  python convert_docx_to_md_python.py <файл.docx>")
            sys.exit(1)
        
        docx_file = str(docx_files[0])
    
    # Проверяем существование входного файла
    if not os.path.exists(docx_file):
        print(f"❌ Ошибка: Файл '{docx_file}' не найден!")
        sys.exit(1)
    
    # Генерируем имена для выходных файлов
    base_name = Path(docx_file).stem
    output_md = f"{base_name}.md"
    images_dir = f"{base_name}_images"
    
    print(f"Конвертация: {docx_file}")
    print(f"Выходной файл: {output_md}")
    print(f"Папка с изображениями: {images_dir}/")
    print("-" * 60)
    
    try:
        image_count = convert_docx_to_markdown(docx_file, output_md, images_dir)
        
        print("-" * 60)
        print(f"✓ Файл успешно конвертирован: {output_md}")
        if image_count > 0:
            print(f"✓ Извлечено изображений: {image_count}")
            print(f"✓ Изображения сохранены в: {images_dir}/")
        else:
            print("ℹ Изображения не найдены в документе")
        
        print(f"\n✓ Готово!")
        
    except Exception as e:
        print(f"❌ Ошибка при конвертации: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
