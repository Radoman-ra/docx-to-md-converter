# Frequently Asked Questions (FAQ)

## General Questions

### What is this tool?
DOCX to Markdown Converter is a command-line utility that converts Microsoft Word documents (.docx) to Markdown format (.md) with automatic image extraction.

### Why would I use this?
- Converting academic papers to Markdown for GitHub
- Migrating documentation to static site generators
- Creating wiki content from Word documents
- Preparing manuscripts for online publication
- Batch processing documents for archival

### Is it free?
Yes! This tool is open-source and licensed under MIT License. Use it freely for personal or commercial projects.

---

## Installation Questions

### Q: Do I need Pandoc?
**A:** No, but recommended. We provide two converters:
- **Pandoc converter** (recommended): Best quality, requires Pandoc
- **Python converter**: No Pandoc needed, basic quality

### Q: How do I install Pandoc?
**A:** 
```bash
# macOS
brew install pandoc

# Ubuntu/Debian
sudo apt-get install pandoc

# Windows
# Download from https://pandoc.org/installing.html
```

### Q: What Python version do I need?
**A:** Python 3.7 or higher. Check your version:
```bash
python3 --version
```

### Q: Can I use this on Windows?
**A:** Yes! The tool works on Windows, macOS, and Linux. On Windows:
1. Install Python 3.7+
2. Install Pandoc (optional)
3. Run: `python convert_docx_to_md.py file.docx`

---

## Usage Questions

### Q: How do I convert a single file?
**A:**
```bash
./convert.sh your-document.docx
```

### Q: Can I convert multiple files at once?
**A:** Yes, use a loop:
```bash
for file in *.docx; do ./convert.sh "$file"; done
```

### Q: Where do the converted files go?
**A:** Same directory as the original:
- `document.docx` → `document.md`
- Images → `document_images/`

### Q: Can I specify output location?
**A:** Currently, no. But you can move files after conversion:
```bash
./convert.sh file.docx
mv file.md output/
mv file_images/ output/
```

### Q: Does it preserve formatting?
**A:** Yes, it preserves:
- ✅ Headers (H1-H6)
- ✅ Bold and italic text
- ✅ Tables
- ✅ Lists (ordered and unordered)
- ✅ Images
- ⚠️ Complex formatting may be simplified

### Q: What about formulas and equations?
**A:** 
- **Pandoc converter**: Preserves formulas as LaTeX
- **Python converter**: Formulas not supported

---

## Technical Questions

### Q: What happens to images?
**A:** All images are:
1. Extracted from .docx file
2. Saved to `<filename>_images/` folder
3. Referenced in Markdown with relative paths

### Q: What image formats are supported?
**A:** Common formats: PNG, JPG, JPEG, GIF, BMP

### Q: How are tables converted?
**A:**
- **Pandoc**: Full table support with proper alignment
- **Python**: Basic tables (simple structure)

### Q: Can I convert password-protected files?
**A:** No, password-protected .docx files are not supported. Remove protection first.

### Q: Does it handle large files?
**A:** Yes! Tested with documents up to 200+ pages. Performance:
- Small (5 pages): ~1 second
- Medium (50 pages): ~3 seconds
- Large (200 pages): ~7 seconds

---

## Troubleshooting

### Q: "pandoc: command not found" error
**A:** Pandoc is not installed. Either:
1. Install Pandoc: `brew install pandoc`
2. Use Python converter: `python3 convert_docx_to_md_python.py file.docx`

### Q: "No module named 'docx'" error
**A:** Install python-docx:
```bash
pip install python-docx
```

### Q: "Permission denied" error
**A:** Make scripts executable:
```bash
chmod +x convert.sh
chmod +x convert_docx_to_md.py
chmod +x convert_docx_to_md_python.py
```

### Q: "File not found" error
**A:** Make sure:
1. The .docx file exists
2. You're in the correct directory
3. The filename is correct (check for spaces)

### Q: Images not extracting
**A:** Check if:
1. Images are actually embedded (not linked)
2. You have write permissions in the directory
3. The .docx file is not corrupted

### Q: Conversion produces empty output
**A:** Possible causes:
1. Empty .docx file
2. Corrupted document
3. Protected/encrypted file
Try opening the file in Word first to verify it's valid.

### Q: Special characters appear wrong
**A:** Ensure UTF-8 encoding. With Pandoc:
```bash
pandoc file.docx -f docx -t markdown -o output.md --wrap=none
```

---

## Feature Questions

### Q: Can it convert to other formats?
**A:** Currently only Markdown. Future versions may support:
- HTML
- PDF
- reStructuredText
- Plain text

### Q: Is there a GUI version?
**A:** Not yet, but it's on the roadmap! Current version is command-line only.

### Q: Can I customize the output?
**A:** Yes, edit the converter scripts to:
- Change output filename pattern
- Modify image folder naming
- Adjust Markdown formatting

### Q: Does it support batch processing?
**A:** Yes, via shell scripts:
```bash
for file in *.docx; do ./convert.sh "$file"; done
```

### Q: Can I integrate it into my project?
**A:** Yes! Import the converters as Python modules:
```python
from convert_docx_to_md_python import convert_docx_to_markdown
convert_docx_to_markdown('input.docx', 'output.md', 'images/')
```

---

## Comparison Questions

### Q: Pandoc vs Python converter - which to use?
**A:**

| Feature | Pandoc | Python |
|---------|--------|--------|
| Quality | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Tables | Excellent | Basic |
| Formulas | Yes | No |
| Installation | Requires Pandoc | Pure Python |
| Speed | Fast | Fast |

**Recommendation:** Use Pandoc for important documents.

### Q: Why not just use Pandoc directly?
**A:** Our tool adds:
- Auto-detection of .docx files
- Better error messages
- Automatic image organization
- Universal wrapper script
- User-friendly interface

### Q: How does this compare to online converters?
**A:**

**Our tool:**
- ✅ Offline/private
- ✅ Batch processing
- ✅ Free
- ✅ No file size limits
- ✅ Customizable

**Online converters:**
- ❌ Privacy concerns
- ❌ File size limits
- ❌ Often paid
- ❌ Requires internet

---

## Performance Questions

### Q: How fast is the conversion?
**A:** Very fast:
- Small docs (5 pages): ~1 second
- Medium docs (50 pages): ~3 seconds
- Large docs (200 pages): ~7 seconds

### Q: How much memory does it use?
**A:** Minimal:
- Small: <50 MB
- Medium: <100 MB
- Large: <200 MB

### Q: Can I convert hundreds of files?
**A:** Yes! Example:
```bash
time for file in *.docx; do ./convert.sh "$file"; done
```

---

## License & Contribution

### Q: Can I use this commercially?
**A:** Yes! MIT License allows commercial use.

### Q: Can I modify the code?
**A:** Yes! Feel free to fork and customize.

### Q: How do I contribute?
**A:** See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Q: Can I report bugs?
**A:** Yes! Open an issue on GitHub with:
- Description of the problem
- Steps to reproduce
- Your environment details

---

## Future Features

### Q: What features are planned?
**A:** Roadmap includes:
- GUI interface
- Configuration file support
- More output formats
- Docker container
- Web API
- Progress bars for batch processing

### Q: When will GUI version be released?
**A:** No specific timeline yet. Follow the project for updates!

### Q: Can I request a feature?
**A:** Yes! Open an issue with your feature request.

---

## Still Have Questions?

- 📖 Read the [full documentation](README.md)
- 💡 Check [examples](EXAMPLES.md)
- 🐛 [Report an issue](https://github.com/your-repo/issues)
- 💬 Start a [discussion](https://github.com/your-repo/discussions)

**Didn't find your answer?** Open an issue and we'll add it to this FAQ!
