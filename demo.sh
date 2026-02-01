#!/bin/bash
# Demo script for DOCX to Markdown Converter
# Shows the tool in action with example output

clear

echo "╔════════════════════════════════════════════════════════════╗"
echo "║     DOCX to Markdown Converter - Demo                     ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Check for demo file
if [ ! -f "example.docx" ] && [ ! -f "*.docx" ]; then
    echo "⚠️  No .docx files found for demo"
    echo ""
    echo "To try the demo:"
    echo "1. Place a .docx file in this directory"
    echo "2. Run: ./demo.sh"
    echo ""
    exit 1
fi

echo "📋 Available Commands:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo "1️⃣  Universal Wrapper (Recommended):"
echo "    ./convert.sh document.docx"
echo ""

echo "2️⃣  Pandoc Converter (Best Quality):"
echo "    python3 convert_docx_to_md.py document.docx"
echo ""

echo "3️⃣  Python Converter (No Dependencies):"
echo "    python3 convert_docx_to_md_python.py document.docx"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check what's installed
echo "🔍 Checking your system:"
echo ""

if command -v pandoc &> /dev/null; then
    PANDOC_VERSION=$(pandoc --version | head -1)
    echo "✅ Pandoc installed: $PANDOC_VERSION"
    PANDOC_AVAILABLE=true
else
    echo "❌ Pandoc not installed"
    echo "   Install: brew install pandoc"
    PANDOC_AVAILABLE=false
fi

if python3 -c "import docx" 2>/dev/null; then
    echo "✅ python-docx installed"
    PYTHON_DOCX_AVAILABLE=true
else
    echo "❌ python-docx not installed"
    echo "   Install: pip install python-docx"
    PYTHON_DOCX_AVAILABLE=false
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Recommendation
echo "💡 Recommendation:"
if [ "$PANDOC_AVAILABLE" = true ]; then
    echo "   Use: ./convert.sh (Will use Pandoc for best quality)"
elif [ "$PYTHON_DOCX_AVAILABLE" = true ]; then
    echo "   Use: python3 convert_docx_to_md_python.py"
else
    echo "   Install dependencies first:"
    echo "   - brew install pandoc (recommended)"
    echo "   - pip install python-docx"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# List available files
echo "📁 Available .docx files:"
DOCX_COUNT=$(ls -1 *.docx 2>/dev/null | wc -l)
if [ "$DOCX_COUNT" -gt 0 ]; then
    ls -lh *.docx 2>/dev/null | awk '{print "   " $9 " (" $5 ")"}'
    echo ""
    echo "To convert, run:"
    echo "   ./convert.sh <filename.docx>"
else
    echo "   No .docx files found"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo "📚 Documentation:"
echo "   README.md       - Main documentation"
echo "   QUICKSTART.md   - Get started in 3 steps"
echo "   EXAMPLES.md     - Usage examples"
echo "   FAQ.md          - Common questions"
echo ""

echo "❓ Need help? Run: cat QUICKSTART.md"
echo ""
