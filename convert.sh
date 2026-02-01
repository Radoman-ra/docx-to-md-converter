#!/bin/bash
# Универсальный скрипт-обертка для конвертации DOCX в Markdown

echo "=========================================="
echo "  Конвертер DOCX в Markdown"
echo "=========================================="
echo ""

# Проверяем наличие pandoc
if command -v pandoc &> /dev/null; then
    echo "✓ Найден pandoc - используем оптимальный метод конвертации"
    echo ""
    python3 convert_docx_to_md.py "$@"
else
    echo "⚠ Pandoc не найден - используем Python метод"
    echo ""
    echo "Для лучшего качества установите pandoc:"
    echo "  brew install pandoc"
    echo ""
    
    # Проверяем наличие python-docx
    if python3 -c "import docx" 2>/dev/null; then
        python3 convert_docx_to_md_python.py "$@"
    else
        echo "❌ Библиотека python-docx не найдена"
        echo ""
        echo "Установите зависимости:"
        echo "  pip3 install python-docx"
        echo ""
        echo "Или установите pandoc:"
        echo "  brew install pandoc"
        exit 1
    fi
fi
