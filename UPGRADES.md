## basic
add pdf splitter
pdf compressor
Glob support: pdfmerge *.pdf -o output.pdf
Directory input: pdfmerge ./documents/ -o output.pdf
Page ranges: pdfmerge file1.pdf[1-5] file2.pdf[3,5-7] -o output.pdf
Order specification: pdfmerge -f file1.pdf file3.pdf file2.pdf -o output.pdf

## intermidiate
Compression options:
    pdfmerge *.pdf -o output.pdf --compress high
    pdfmerge *.pdf -o output.pdf --quality draft
Metadata editing:
    pdfmerge *.pdf -o output.pdf --title "Report" --author "John Doe"
Password protection:
    pdfmerge *.pdf -o output.pdf --encrypt --password "secret"
Bookmark generation:
    pdfmerge *.pdf -o output.pdf --bookmarks

## advanced
Smart filtering:
    # Only merge files > 1MB
    pdfmerge *.pdf --min-size 1MB -o output.pdf
    # Merge newest 5 files
    pdfmerge *.pdf --newest 5 -o output.pdf
Page manipulation:
    # Rotate every 2nd page
    pdfmerge *.pdf --rotate-even 90 -o output.pdf
    # Insert blank pages between files
    pdfmerge *.pdf --separators -o output.pdf
Watermarking:
    pdfmerge *.pdf --watermark "CONFIDENTIAL" -o output.pdf
    pdfmerge *.pdf --watermark-file stamp.pdf -o output.pdf
Split during merge:
    # Split output by page count
    pdfmerge *.pdf --split-every 50 -o output_prefix
    # Split by file size
    pdfmerge *.pdf --max-size 10MB -o output_prefix
Progress indicators:
    pdfmerge large*.pdf -o output.pdf --progress --verbose


## Output & Format Options
Multiple output formats:
    pdfmerge *.pdf -o report --format pdfa  # PDF/A for archiving
    pdfmerge *.pdf -o images --format png   # Extract pages as images
Batch processing:
    # Process multiple merge jobs from a file
    pdfmerge --batch jobs.txt
Validation & repair:
    pdfmerge corrupted.pdf -o fixed.pdf --repair