# Contributing to DOCX to Markdown Converter

First off, thank you for considering contributing to this project! 🎉

## How Can I Contribute?

### Reporting Bugs

If you find a bug, please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version, Pandoc version)
- Sample .docx file (if possible)

### Suggesting Enhancements

Have an idea? Open an issue with:
- Clear description of the enhancement
- Why it would be useful
- Examples of how it would work

### Pull Requests

1. Fork the repo
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit with clear message (`git commit -m 'Add amazing feature'`)
6. Push to your fork (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/docx-to-md-converter.git
cd docx-to-md-converter

# Install dependencies
pip install -r requirements.txt

# Install Pandoc (for testing)
brew install pandoc  # macOS
```

## Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small
- Add docstrings for functions

## Testing

Before submitting a PR:
- Test with various .docx files
- Test both conversion methods (Pandoc and Python)
- Verify image extraction works
- Check error handling

## Documentation

If you add features:
- Update README.md
- Add usage examples
- Update relevant documentation files

## Questions?

Feel free to open an issue for any questions!

Thank you for contributing! 🙏
