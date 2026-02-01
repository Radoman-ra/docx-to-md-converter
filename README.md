# 📄 DOCX to Markdown Converter

<div align="center">

**A powerful and flexible tool to convert Microsoft Word documents to Markdown with automatic image extraction**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)]()

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Examples](#-examples) • [Documentation](#-documentation)

</div>

---

## 🎯 About The Project

DOCX to Markdown Converter is a versatile command-line tool that transforms Microsoft Word documents (.docx) into clean, well-formatted Markdown files. It automatically extracts and organizes all embedded images, making it perfect for:

- 📚 Converting academic papers and theses to Markdown
- 📝 Migrating documentation from Word to static site generators
- 💼 Creating GitHub-friendly README files from existing docs
- 🔄 Batch processing multiple documents
- 🎓 Preparing manuscripts for online publication

### Why This Project?

While many converters exist, this tool offers:
- **Two conversion methods**: Pandoc (best quality) and pure Python (no dependencies)
- **Automatic image extraction**: All images saved with proper references
- **Smart auto-detection**: Automatically finds .docx files in current directory
- **Preservation of formatting**: Headers, bold, italic, tables, and lists
- **Flexible usage**: Command-line interface or universal wrapper script

---

## ✨ Features

- ✅ **Dual Conversion Engines**
  - Pandoc-based converter for professional-grade output
  - Pure Python converter for dependency-free operation
  
- 🖼️ **Image Handling**
  - Automatic extraction of all embedded images
  - Organized storage in dedicated folders
  - Relative path references in Markdown
  - Supports PNG, JPG, JPEG, GIF formats

- 📋 **Rich Format Support**
  - Headers (H1-H6)
  - Bold and italic text
  - Tables with proper alignment
  - Ordered and unordered lists
  - Mathematical formulas (Pandoc mode)

- 🚀 **User-Friendly**
  - Auto-detection of .docx files
  - Universal wrapper script
  - Clear error messages and instructions
  - Cross-platform compatibility

---

## 🛠️ Tech Stack

**Core Technologies:**
- Python 3.7+
- Pandoc 2.0+ (optional, recommended)

**Python Libraries:**
- `python-docx` - Pure Python DOCX parser
- `pypandoc` - Python wrapper for Pandoc

**Supported Platforms:**
- macOS (Homebrew)
- Linux (apt/yum)
- Windows (manual install)

---

## 📦 Installation

### Quick Start (Recommended)

```bash
# Clone or download the converter
cd "docx to md converter"

# Install Pandoc (best quality)
brew install pandoc  # macOS
# sudo apt-get install pandoc  # Ubuntu/Debian

# Run conversion
./convert.sh your-document.docx
```

### Alternative: Pure Python Method

```bash
# Install Python dependencies only
pip install -r requirements.txt

# Run Python converter
python3 convert_docx_to_md_python.py your-document.docx
```

### Detailed Installation

<details>
<summary>Click to expand installation instructions</summary>

#### Installing Pandoc

**macOS:**
```bash
brew install pandoc
```

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install pandoc
```

**Windows:**
Download from [pandoc.org](https://pandoc.org/installing.html)

#### Installing Python Dependencies

```bash
pip install python-docx
# or install all at once
pip install -r requirements.txt
```

</details>

---

## 🚀 Usage

### Basic Usage

```bash
# Using universal wrapper (automatically chooses best method)
./convert.sh document.docx

# Using Pandoc converter directly
python3 convert_docx_to_md.py document.docx

# Using Python converter directly
python3 convert_docx_to_md_python.py document.docx
```

### Auto-Detection

If you have a single .docx file in the directory:

```bash
./convert.sh
# Automatically finds and converts the .docx file
```

### Output Structure

```
your-directory/
├── YourDocument.docx          # Original file
├── YourDocument.md            # ✨ Converted Markdown
└── YourDocument_images/       # ✨ Extracted images
    ├── image1.png
    ├── image2.jpg
    └── ...
```

---

## 💡 Examples

### Example 1: Converting a Thesis

```bash
./convert.sh DiplomaThesis.docx
```

**Output:**
```
✓ Файл успешно конвертирован: DiplomaThesis.md
✓ Извлечено изображений: 42
✓ Изображения сохранены в: DiplomaThesis_images/
```

### Example 2: Batch Conversion

```bash
# Convert all .docx files in directory
for file in *.docx; do
    ./convert.sh "$file"
done
```

### Example 3: Specific File Path

```bash
python3 convert_docx_to_md.py /path/to/document.docx
```

---

## 📁 Project Structure

```
docx to md converter/
│
├── convert.sh                      # Universal wrapper script (USE THIS!)
├── convert_docx_to_md.py          # Pandoc-based converter
├── convert_docx_to_md_python.py   # Pure Python converter
│
├── README.md                       # This file
├── QUICKSTART.md                  # Quick reference guide
├── SETUP.md                       # Detailed installation instructions
├── README_CONVERTER.md            # Technical documentation
├── CONVERTER_FILES.md             # File descriptions
│
└── requirements.txt               # Python dependencies
```

---

## 🔧 Advanced Configuration

### Customizing Output

Edit the converter scripts to customize:

**Change image folder name:**
```python
# In convert_docx_to_md.py or convert_docx_to_md_python.py
images_dir = f"{base_name}_images"  # Change to your preference
```

**Change output filename:**
```python
output_md = f"{base_name}.md"  # Customize the pattern
```

### Pandoc Options

The Pandoc converter uses these options by default:
```bash
pandoc \
  --from=docx \
  --to=markdown \
  --extract-media=<images_dir> \
  --wrap=none \
  --output=<output_file>
```

---

## 📊 Comparison: Pandoc vs Python

| Feature | Pandoc Converter | Python Converter |
|---------|------------------|------------------|
| **Quality** | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐ Good |
| **Tables** | Perfect formatting | Basic support |
| **Lists** | Full support | Full support |
| **Images** | Auto-extracted | Auto-extracted |
| **Formulas** | Supported | Not supported |
| **Installation** | Requires Pandoc | Pure Python |
| **Speed** | Fast | Fast |
| **Dependencies** | External program | Python only |

**Recommendation:** Use Pandoc converter for important documents (theses, papers). Use Python converter for quick conversions or when Pandoc is unavailable.

---

## 📚 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Get started in 3 steps
- **[SETUP.md](SETUP.md)** - Detailed installation guide
- **[README_CONVERTER.md](README_CONVERTER.md)** - Technical deep-dive
- **[CONVERTER_FILES.md](CONVERTER_FILES.md)** - File-by-file description

---

## 🐛 Troubleshooting

### Common Issues

<details>
<summary><b>"pandoc: command not found"</b></summary>

**Solution:**
```bash
brew install pandoc  # macOS
sudo apt-get install pandoc  # Linux
```
</details>

<details>
<summary><b>"No module named 'docx'"</b></summary>

**Solution:**
```bash
pip install python-docx
```
</details>

<details>
<summary><b>"Permission denied"</b></summary>

**Solution:**
```bash
chmod +x convert.sh
chmod +x convert_docx_to_md.py
chmod +x convert_docx_to_md_python.py
```
</details>

<details>
<summary><b>"File not found"</b></summary>

**Solution:**
Make sure the .docx file is in the current directory or provide full path:
```bash
./convert.sh /full/path/to/document.docx
```
</details>

---

## 🧪 Testing

Tested with:
- ✅ Academic theses (10-200 pages)
- ✅ Technical documentation
- ✅ Reports with tables and images
- ✅ Documents with complex formatting
- ✅ Multiple languages (English, Russian, etc.)

---

## 🎯 Use Cases

### Academic Writing
```bash
# Convert thesis to Markdown for GitHub
./convert.sh thesis.docx
```

### Documentation Migration
```bash
# Batch convert company docs
for doc in documentation/*.docx; do
    ./convert.sh "$doc"
done
```

### Blog Publishing
```bash
# Convert article drafts
./convert.sh "Blog Post Draft.docx"
# Upload YourPost.md to static site generator
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the project
2. 🌿 Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔃 Open a Pull Request

### Ideas for Contributions
- Add support for more output formats (HTML, PDF)
- Implement GUI interface
- Add batch processing with progress bar
- Support for additional image formats
- Custom styling options for output

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Max Andzheychak**

- GitHub: [@your-github](https://github.com/your-username)
- Email: your.email@example.com

---

## 🙏 Acknowledgments

- [Pandoc](https://pandoc.org/) - Universal document converter
- [python-docx](https://python-docx.readthedocs.io/) - Python library for .docx files
- All contributors and users of this tool

---

## 📈 Project Stats

- **Lines of Code:** ~500
- **Languages:** Python, Shell
- **Documentation:** 5 comprehensive guides
- **Platform Support:** Cross-platform

---

## 🗺️ Roadmap

- [x] Basic DOCX to Markdown conversion
- [x] Image extraction and organization
- [x] Dual converter engines
- [x] Auto-detection of files
- [x] Comprehensive documentation
- [ ] GUI interface
- [ ] Batch processing with progress bars
- [ ] Configuration file support
- [ ] Docker containerization
- [ ] Web API endpoint

---

<div align="center">

**⭐ If you find this project helpful, please give it a star! ⭐**

Made with ❤️ by developers, for developers

[Report Bug](https://github.com/your-repo/issues) · [Request Feature](https://github.com/your-repo/issues)

</div>
