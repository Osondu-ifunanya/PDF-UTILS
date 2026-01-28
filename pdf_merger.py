#!/usr/bin/env python3
"""
PDF Merger Utility
Merges multiple PDF files into a single PDF document.
"""

import sys
import os
from pathlib import Path

try:
    from PyPDF2 import PdfMerger
except ImportError:
    print("Error: PyPDF2 is not installed.")
    print("Install it with: pip install PyPDF2")
    sys.exit(1)


def merge_pdfs(pdf_files, output_file):
    """
    Merge multiple PDF files into one.
    
    Args:
        pdf_files: List of PDF file paths to merge
        output_file: Output PDF file path
    """
    merger = PdfMerger()
    
    for pdf_file in pdf_files:
        if not os.path.exists(pdf_file):
            print(f"Warning: File not found - {pdf_file}")
            continue
        
        if not pdf_file.lower().endswith('.pdf'):
            print(f"Warning: Skipping non-PDF file - {pdf_file}")
            continue
        
        try:
            merger.append(pdf_file)
            print(f"Added: {pdf_file}")
        except Exception as e:
            print(f"Error adding {pdf_file}: {e}")
    
    try:
        merger.write(output_file)
        merger.close()
        print(f"\nSuccess! Merged PDF saved to: {output_file}")
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) < 3:
        print("Usage: python pdf_merger.py <output.pdf> <input1.pdf> <input2.pdf> ...")
        print("\nExample:")
        print("  python pdf_merger.py merged.pdf file1.pdf file2.pdf file3.pdf")
        sys.exit(1)
    
    output_file = sys.argv[1]
    input_files = sys.argv[2:]
    
    if not output_file.lower().endswith('.pdf'):
        output_file += '.pdf'
    
    print(f"Merging {len(input_files)} PDF files...")
    merge_pdfs(input_files, output_file)


if __name__ == "__main__":
    main()
