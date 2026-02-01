#!/usr/bin/env python3
"""
Скрипт для конвертации DOCX в Markdown с извлечением изображений

Использование:
    python convert_docx_to_md.py [файл.docx]
    
Если файл не указан, скрипт автоматически найдет .docx файл в текущей директории.

Требования:
    - pandoc (brew install pandoc на macOS)
    - или pypandoc (pip install pypandoc)
"""

import os
import sys
import subprocess
from pathlib import Path

def check_pandoc():
    """Проверка наличия pandoc"""
    try:
        result = subprocess.run(['pandoc', '--version'], 
                              capture_output=True, 
                              text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def convert_with_pandoc(docx_file, output_md, images_dir):
    """Конвертация с помощью pandoc"""
    # Создаем директорию для изображений
    images_path = Path(images_dir)
    images_path.mkdir(exist_ok=True)
    
    # Конвертируем с помощью pandoc
    cmd = [
        'pandoc',
        docx_file,
        '-f', 'docx',
        '-t', 'markdown',
        '--extract-media', images_dir,
        '-o', output_md,
        '--wrap=none'
    ]
    
    print(f"Запуск pandoc...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Ошибка при конвертации: {result.stderr}")
        return False
    
    print(f"✓ Файл успешно конвертирован: {output_md}")
    if images_path.exists() and any(images_path.iterdir()):
        print(f"✓ Изображения извлечены в: {images_dir}")
    else:
        print("ℹ Изображения не найдены в документе")
    
    return True

def install_pandoc_instructions():
    """Инструкции по установке pandoc"""
    print("\n" + "="*60)
    print("PANDOC НЕ УСТАНОВЛЕН")
    print("="*60)
    print("\nДля установки pandoc выполните:")
    print("\nmacOS:")
    print("  brew install pandoc")
    print("\nLinux (Ubuntu/Debian):")
    print("  sudo apt-get install pandoc")
    print("\nWindows:")
    print("  Скачайте с https://pandoc.org/installing.html")
    print("\nИли используйте pip:")
    print("  pip install pypandoc")
    print("="*60 + "\n")

def main():
    # Проверяем аргументы командной строки
    if len(sys.argv) > 1:
        docx_file = sys.argv[1]
    else:
        # Ищем .docx файлы в текущей директории
        docx_files = list(Path('.').glob('*.docx'))
        if not docx_files:
            print("❌ Ошибка: Файлы .docx не найдены!")
            print("\nИспользование:")
            print("  python convert_docx_to_md.py <файл.docx>")
            print("  или просто запустите скрипт в папке с .docx файлом")
            sys.exit(1)
        
        if len(docx_files) > 1:
            print("Найдено несколько .docx файлов:")
            for i, f in enumerate(docx_files, 1):
                print(f"  {i}. {f}")
            print("\nУкажите файл явно:")
            print("  python convert_docx_to_md.py <файл.docx>")
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
    
    # Проверяем наличие pandoc
    if not check_pandoc():
        install_pandoc_instructions()
        
        # Пробуем использовать pypandoc
        try:
            import pypandoc
            print("Найден pypandoc, пробуем конвертировать...")
            
            # Создаем директорию для изображений
            Path(images_dir).mkdir(exist_ok=True)
            
            # Конвертируем
            output = pypandoc.convert_file(
                docx_file,
                'md',
                extra_args=['--extract-media', images_dir, '--wrap=none']
            )
            
            # Сохраняем результат
            with open(output_md, 'w', encoding='utf-8') as f:
                f.write(output)
            
            print(f"✓ Файл успешно конвертирован: {output_md}")
            sys.exit(0)
            
        except ImportError:
            print("\n❌ Установите pandoc или pypandoc для конвертации")
            print("   pip install pypandoc")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Ошибка при конвертации: {e}")
            sys.exit(1)
    
    # Конвертируем с помощью pandoc
    success = convert_with_pandoc(docx_file, output_md, images_dir)
    
    if success:
        print(f"\n✓ Готово!")
        print(f"  Markdown файл: {output_md}")
        print(f"  Изображения: {images_dir}/")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
