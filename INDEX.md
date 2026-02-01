# 📚 Documentation Index

> **Quick navigation guide for DOCX to Markdown Converter**

---

## 🚀 Getting Started

<table>
<tr>
<td width="50%">

### New Users Start Here

1. 📖 **[README.md](README.md)**  
   *Main documentation - overview of everything*

2. ⚡ **[QUICKSTART.md](QUICKSTART.md)**  
   *Get running in 3 steps*

3. 🎯 **Run your first conversion:**
   ```bash
   ./convert.sh your-file.docx
   ```

</td>
<td width="50%">

### Key Features

✅ Two conversion engines  
✅ Automatic image extraction  
✅ Headers, tables, lists support  
✅ Cross-platform compatible  
✅ Batch processing capable  
✅ MIT License (free!)

</td>
</tr>
</table>

---

## 📖 Full Documentation

| Document | Purpose | When to Read |
|----------|---------|--------------|
| **[README.md](README.md)** | Complete project overview | First time setup |
| **[QUICKSTART.md](QUICKSTART.md)** | 3-step quick start | Want to start NOW |
| **[SETUP.md](SETUP.md)** | Detailed installation | Need help installing |
| **[EXAMPLES.md](EXAMPLES.md)** | Real-world usage | Want to learn more |
| **[FAQ.md](FAQ.md)** | Common questions | Have a question |
| **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** | Project organization | Want to understand structure |
| **[CONTRIBUTING.md](CONTRIBUTING.md)** | Contribution guide | Want to contribute |
| **[CHANGELOG.md](CHANGELOG.md)** | Version history | Track updates |

---

## 🛠️ Core Tools

### Main Scripts

```bash
# 🌟 Universal Wrapper (USE THIS!)
./convert.sh document.docx

# 📄 Pandoc Converter (Best Quality)
python3 convert_docx_to_md.py document.docx

# 🐍 Python Converter (No Pandoc Needed)
python3 convert_docx_to_md_python.py document.docx

# 🎬 Demo Script
./demo.sh
```

---

## 💡 Quick Reference

### Installation

```bash
# Install Pandoc (recommended)
brew install pandoc

# Install Python library
pip install python-docx

# Or install all at once
pip install -r requirements.txt
```

### Basic Usage

```bash
# Convert single file
./convert.sh document.docx

# Auto-detect and convert
./convert.sh

# Batch convert all .docx files
for file in *.docx; do ./convert.sh "$file"; done
```

### Output

```
document.docx           → document.md
                        → document_images/
                          ├── image1.png
                          ├── image2.jpg
                          └── ...
```

---

## 🎯 Choose Your Path

<table>
<tr>
<td width="33%">

### 🎓 Academic User
*Converting thesis or paper*

1. Read [README.md](README.md)
2. Install Pandoc
3. Run conversion
4. Check [FAQ.md](FAQ.md) if needed

</td>
<td width="33%">

### 💼 Professional User
*Processing documents*

1. Read [QUICKSTART.md](QUICKSTART.md)
2. Install dependencies
3. See [EXAMPLES.md](EXAMPLES.md)
4. Set up batch processing

</td>
<td width="33%">

### 👨‍💻 Developer
*Want to contribute*

1. Read [README.md](README.md)
2. Check [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)
3. Read [CONTRIBUTING.md](CONTRIBUTING.md)
4. Start coding!

</td>
</tr>
</table>

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| "pandoc not found" | Install: `brew install pandoc` |
| "No module 'docx'" | Install: `pip install python-docx` |
| "Permission denied" | Run: `chmod +x *.sh *.py` |
| Other issues | Check [FAQ.md](FAQ.md) |

---

## 📊 Project Stats

```
Version:        1.0.0
License:        MIT
Languages:      Python, Shell
Lines of Code:  ~2,600
Documentation:  8 comprehensive guides
Platform:       macOS, Linux, Windows
```

---

## 🌟 Key Highlights

### Why This Tool?

- **Two conversion methods**: Choose quality (Pandoc) or simplicity (Python)
- **Smart auto-detection**: Finds .docx files automatically
- **Image handling**: Extracts and organizes all images
- **Well documented**: 8 guides covering everything
- **Production ready**: Tested with 200+ page documents
- **Free & Open**: MIT License, use anywhere

### What Gets Converted?

✅ Headers (H1-H6)  
✅ Bold and italic text  
✅ Tables  
✅ Lists (ordered & unordered)  
✅ Images (all formats)  
✅ Formulas (with Pandoc)

---

## 📞 Need Help?

1. **Questions?** → [FAQ.md](FAQ.md)
2. **Installation?** → [SETUP.md](SETUP.md)
3. **Examples?** → [EXAMPLES.md](EXAMPLES.md)
4. **Bug report?** → Open GitHub Issue
5. **Feature request?** → Open GitHub Issue

---

## 🗺️ Documentation Map

```
┌─────────────────────────────────────────────────────────┐
│                      README.md                          │
│              (START HERE - Main Overview)               │
└─────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ QUICKSTART   │    │    SETUP     │    │   EXAMPLES   │
│   (Fast)     │    │  (Detailed)  │    │  (Advanced)  │
└──────────────┘    └──────────────┘    └──────────────┘
        │                   │                   │
        └───────────────────┼───────────────────┘
                            │
                            ▼
                    ┌──────────────┐
                    │     FAQ      │
                    │  (Problems)  │
                    └──────────────┘
```

---

## 🎬 Quick Start Commands

```bash
# 1. Check what you have
./demo.sh

# 2. Install if needed
brew install pandoc
pip install python-docx

# 3. Convert!
./convert.sh your-document.docx

# 4. Check output
ls -l *.md *_images/
```

---

## 📦 What's Included

### Scripts (3)
- `convert.sh` - Universal wrapper
- `convert_docx_to_md.py` - Pandoc converter  
- `convert_docx_to_md_python.py` - Python converter

### Documentation (8)
- README, QUICKSTART, SETUP, EXAMPLES
- FAQ, CONTRIBUTING, CHANGELOG, PROJECT_STRUCTURE

### Utilities (3)
- `requirements.txt` - Dependencies
- `LICENSE` - MIT License
- `demo.sh` - Interactive demo

---

## 🏆 Best Practices

1. **For important docs**: Use Pandoc converter
2. **Test first**: Try with a small file
3. **Backup originals**: Keep .docx files safe
4. **Check output**: Review .md file after conversion
5. **Report issues**: Help improve the tool

---

<div align="center">

## Ready to Start?

**[📖 Read README](README.md)** • **[⚡ Quick Start](QUICKSTART.md)** • **[🎬 Run Demo](demo.sh)**

---

Made with ❤️ for document conversion

**v1.0.0** • MIT License • 2026

</div>
