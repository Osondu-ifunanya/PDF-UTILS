# PDF Merger Utility

A simple command-line tool to merge multiple PDF files into a single document.

## Installation

1. Create and activate a virtual environment (if not already done):
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```bash
python pdf_merger.py <output.pdf> <input1.pdf> <input2.pdf> ...
```

### Example

```bash
python pdf_merger.py merged.pdf document1.pdf document2.pdf document3.pdf
```

This will create `merged.pdf` containing all the input PDFs in the order specified.

## Features

- Merge multiple PDFs in specified order
- Validates input files
- Clear error messages
- Simple command-line interface
