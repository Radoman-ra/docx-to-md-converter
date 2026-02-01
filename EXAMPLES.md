# Usage Examples

This document provides practical examples of using the DOCX to Markdown Converter.

## Table of Contents
- [Basic Usage](#basic-usage)
- [Academic Documents](#academic-documents)
- [Batch Processing](#batch-processing)
- [Advanced Scenarios](#advanced-scenarios)
- [Integration Examples](#integration-examples)

---

## Basic Usage

### Convert a Single File

```bash
# Using universal wrapper (recommended)
./convert.sh document.docx

# Using Pandoc converter
python3 convert_docx_to_md.py document.docx

# Using Python converter
python3 convert_docx_to_md_python.py document.docx
```

### Auto-Detect and Convert

```bash
# If you have one .docx file in the directory
./convert.sh

# Output:
# Конвертация: YourDocument.docx
# ✓ Файл успешно конвертирован: YourDocument.md
# ✓ Извлечено изображений: 15
```

---

## Academic Documents

### Convert Thesis or Dissertation

```bash
./convert.sh "PhD_Thesis_Final_v3.docx"
```

**Result:**
```
PhD_Thesis_Final_v3.md
PhD_Thesis_Final_v3_images/
├── image1.png    # Figure 1: Research Framework
├── image2.png    # Table 1: Results
├── image3.jpg    # Diagram of methodology
└── ...
```

### Convert Research Paper

```bash
python3 convert_docx_to_md.py "Research_Paper_2026.docx"
```

**What gets converted:**
- Abstract
- Introduction with citations
- Tables with data
- Figures and charts
- References section
- Appendices

---

## Batch Processing

### Convert All DOCX Files in Directory

```bash
for file in *.docx; do
    echo "Converting: $file"
    ./convert.sh "$file"
done
```

### Convert with Custom Naming

```bash
for file in *.docx; do
    base=$(basename "$file" .docx)
    python3 convert_docx_to_md.py "$file"
    mv "${base}.md" "converted_${base}.md"
done
```

### Convert Files from Subdirectories

```bash
find . -name "*.docx" -type f | while read file; do
    echo "Processing: $file"
    ./convert.sh "$file"
done
```

---

## Advanced Scenarios

### Convert with Full Path

```bash
python3 convert_docx_to_md.py "/Users/john/Documents/Reports/Annual_Report_2025.docx"
```

### Process and Move to Output Directory

```bash
#!/bin/bash
INPUT_DIR="./input_docs"
OUTPUT_DIR="./converted_docs"

mkdir -p "$OUTPUT_DIR"

for doc in "$INPUT_DIR"/*.docx; do
    ./convert.sh "$doc"
    base=$(basename "$doc" .docx)
    mv "${base}.md" "$OUTPUT_DIR/"
    mv "${base}_images" "$OUTPUT_DIR/" 2>/dev/null || true
done

echo "All documents converted and moved to $OUTPUT_DIR"
```

### Convert with Error Handling

```bash
#!/bin/bash
LOG_FILE="conversion_log.txt"

for file in *.docx; do
    echo "[$(date)] Converting: $file" >> "$LOG_FILE"
    
    if ./convert.sh "$file" >> "$LOG_FILE" 2>&1; then
        echo "[$(date)] ✓ Success: $file" >> "$LOG_FILE"
    else
        echo "[$(date)] ✗ Failed: $file" >> "$LOG_FILE"
    fi
done
```

---

## Integration Examples

### Hugo Static Site Generator

```bash
# Convert blog post
./convert.sh "blog-post-draft.docx"

# Add front matter and move to Hugo
cat > temp.md << EOF
---
title: "My Blog Post"
date: $(date +%Y-%m-%d)
draft: false
---

EOF

cat blog-post-draft.md >> temp.md
mv temp.md ~/hugo-site/content/posts/my-blog-post.md
cp -r blog-post-draft_images/ ~/hugo-site/static/images/
```

### Jekyll Site

```bash
# Convert and prepare for Jekyll
./convert.sh article.docx

# Add YAML front matter
sed -i '' '1s/^/---\nlayout: post\ntitle: "Article Title"\ndate: '$(date +%Y-%m-%d)'\n---\n\n/' article.md

# Move to Jekyll
mv article.md ~/jekyll-site/_posts/$(date +%Y-%m-%d)-article.md
```

### GitHub Wiki

```bash
# Convert documentation
./convert.sh "User-Guide.docx"

# Clone wiki
git clone https://github.com/user/repo.wiki.git

# Add converted file
cp User-Guide.md repo.wiki/
cp -r User-Guide_images/ repo.wiki/images/

# Commit and push
cd repo.wiki
git add .
git commit -m "Add user guide"
git push
```

### Obsidian Vault

```bash
# Convert notes to Obsidian
./convert.sh "Meeting-Notes.docx"

# Move to vault
VAULT_PATH="$HOME/Obsidian/MyVault"
mv Meeting-Notes.md "$VAULT_PATH/"
mv Meeting-Notes_images/ "$VAULT_PATH/attachments/"
```

---

## Real-World Examples

### Example 1: Diploma Thesis

```bash
# Original file: DiplomaThesis.docx (24,757 lines, 15 MB)
./convert.sh DiplomaThesis.docx

# Result:
# ✓ DiplomaThesis.md created (1,220 lines, 44 KB)
# ✓ 42 images extracted (7.6 MB total)
# ✓ All tables, headers, and formatting preserved
```

### Example 2: Technical Documentation

```bash
# Convert API documentation
python3 convert_docx_to_md.py "API-Documentation-v2.docx"

# Result includes:
# - Code examples (as text blocks)
# - API endpoint tables
# - Request/response examples
# - Architecture diagrams
```

### Example 3: Weekly Reports

```bash
# Batch convert weekly reports
for week in Week_{1..12}.docx; do
    ./convert.sh "$week"
done

# Organize by month
mkdir -p Reports/January Reports/February Reports/March
mv Week_{1..4}.md Reports/January/
mv Week_{5..8}.md Reports/February/
mv Week_{9..12}.md Reports/March/
```

---

## Troubleshooting Examples

### Problem: Large File Takes Too Long

```bash
# Solution: Use Pandoc method (faster for large files)
python3 convert_docx_to_md.py large-document.docx
```

### Problem: Images Not Extracting

```bash
# Check if images exist in document
python3 -c "
from docx import Document
doc = Document('your-file.docx')
rels = doc.part.rels
for rel in rels.values():
    if 'image' in rel.target_ref:
        print(f'Found image: {rel.target_ref}')
"
```

### Problem: Special Characters Not Converting

```bash
# Use Pandoc with UTF-8 encoding
pandoc document.docx \
    --from=docx \
    --to=markdown \
    --output=document.md \
    --extract-media=images \
    --wrap=none \
    --eol=lf
```

---

## Performance Examples

### Benchmark Results

```
Small document (5 pages, 2 images):
- Pandoc: ~1 second
- Python: ~1 second

Medium document (50 pages, 20 images):
- Pandoc: ~3 seconds
- Python: ~4 seconds

Large document (200 pages, 42 images):
- Pandoc: ~7 seconds
- Python: ~8 seconds
```

### Memory Usage

```
Small: <50 MB RAM
Medium: <100 MB RAM
Large: <200 MB RAM
```

---

## Tips and Tricks

### Tip 1: Preview Before Converting

```bash
# Check document structure
python3 -c "
from docx import Document
doc = Document('file.docx')
for para in doc.paragraphs[:10]:
    print(f'{para.style.name}: {para.text[:50]}...')
"
```

### Tip 2: Quick Quality Check

```bash
# After conversion, check line count
wc -l output.md
# Check image count
ls -1 output_images/ | wc -l
```

### Tip 3: Clean Up After Conversion

```bash
# Remove original .docx after successful conversion
./convert.sh file.docx && rm file.docx
```

---

## Questions?

If you have more use cases or examples to share, please contribute to this document!

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute.
