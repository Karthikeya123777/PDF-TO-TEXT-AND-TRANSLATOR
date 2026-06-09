# PDF to Text Converter with Translation

A Python-based desktop application that extracts text from PDF files and translates it to multiple languages using a user-friendly graphical interface.

## 📋 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Troubleshooting](#troubleshooting)
- [Future Improvements](#future-improvements)

## ✨ Features

- **PDF Text Extraction**: Extract text from PDF files using `pdfplumber`
- **Multi-language Translation**: Translate extracted text to over 100 languages using Google Translate
- **User-Friendly GUI**: Clean and intuitive Tkinter-based interface
- **Side-by-Side Comparison**: View original and translated text simultaneously
- **Language Selection**: Choose from a comprehensive list of supported languages
- **Automatic Language Detection**: Automatically detects the source language

## 📦 Requirements

### System Requirements
- Python 3.7 or higher
- Windows, macOS, or Linux
- Internet connection (for translation service)

### Python Dependencies
- `pdfplumber` - PDF text extraction
- `deep-translator` - Google Translate integration
- `tkinter` - GUI framework (usually included with Python)

## 🚀 Installation

### Step 1: Clone or Download the Repository
```bash
git clone <repository-url>
cd "Text to pdf convertor"
```

### Step 2: Create a Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install pdfplumber deep-translator
```

Or install from a requirements file (if available):
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Running the Application

1. **Activate your virtual environment** (if using one):
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

2. **Run the main application**:
   ```bash
   python project.py
   ```

### Using the Application

1. **Launch the Application**: Run `project.py` to open the TransPDF window
2. **Upload PDF**: Click the "Upload PDF" button and select your PDF file
3. **View Extracted Text**: The extracted text will appear in the left panel
4. **Select Target Language**: Choose your desired translation language from the dropdown menu
5. **Translate**: Click the "Translate" button to translate the text
6. **View Translation**: The translated text will appear in the right panel

### Example Workflow

```
1. Click "Upload PDF" → Select your PDF file
2. Wait for text extraction (automatic)
3. Select target language (e.g., "Spanish", "French", "Hindi")
4. Click "Translate"
5. View both original and translated text side by side
```

## 📁 Project Structure

```
Text to pdf convertor/
│
├── project.py                    # Main application (Tkinter GUI)
├── pdf_to_text_converter.py     # (Empty - placeholder)
├── Untitled.ipynb               # Jupyter notebook version (experimental)
├── README.md                    # This file
│
├── venv/                        # Virtual environment (excluded from git)
├── .ipynb_checkpoints/          # Jupyter notebook checkpoints
│
├── AI/                          # Separate AI project folder
│   ├── backend/
│   ├── requirements.txt
│   └── README.md
│
└── ai-landing-page-generator/   # Separate project folder
    ├── backend/
    ├── requirements.txt
    └── README.md
```

## 🛠️ Technologies Used

- **Python 3.x**: Programming language
- **Tkinter**: GUI framework for desktop application
- **pdfplumber**: PDF text extraction library
- **deep-translator**: Google Translate API wrapper for translations

## ⚠️ Troubleshooting

### Common Issues

#### 1. ModuleNotFoundError
If you encounter `ModuleNotFoundError` for any package:
```bash
pip install pdfplumber deep-translator
```

#### 2. Tkinter Not Found
If `tkinter` is not available (rare on Linux):
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter
```

#### 3. Translation Errors
- Ensure you have an active internet connection
- Google Translate API may have rate limits for free usage
- Large texts may take longer to translate

#### 4. PDF Extraction Issues
- Some PDFs with images or scanned content may not extract text properly
- PDFs with complex layouts may require additional processing
- Ensure the PDF is not password-protected

#### 5. Jupyter Notebook Version (Untitled.ipynb)
The Jupyter notebook version uses different libraries (`googletrans`, `PyMuPDF`) and may have compatibility issues with Python 3.13 due to the deprecated `cgi` module. For best results, use the main `project.py` application.

## 🔮 Future Improvements

- [ ] Export translated text to PDF
- [ ] Save extracted text to file
- [ ] Batch processing for multiple PDFs
- [ ] OCR support for scanned PDFs
- [ ] Progress bar for large files
- [ ] Dark mode theme
- [ ] Copy to clipboard functionality
- [ ] Support for other translation services
- [ ] Command-line interface option

## 📝 Notes

- The application requires an internet connection for translation services
- Translation quality depends on Google Translate's service
- Large PDF files may take longer to process
- The Jupyter notebook version (`Untitled.ipynb`) is experimental and may have compatibility issues

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available for personal and educational use.

## 👤 Author

Created as a PDF translation tool for extracting and translating text from PDF documents.

---

**Note**: This project focuses on the PDF to text conversion and translation functionality. The `AI/` and `ai-landing-page-generator/` folders contain separate projects and are not part of the main PDF translator application.

