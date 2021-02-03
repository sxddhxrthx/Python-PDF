# Python-PDF
Python program to split a PDF file into multiple PDF files and to merge multiple PDF files into single PDF file.

## Usage:

### Merging files

In order to merge multiple PDF files into a single file, open command prompt/terminal window and type the below command and press enter:

> **python mergepdf.py "absolute/path/to/firstpdf" "absolute/path/to/secondpdf" ["absolute/path/to/otherpdf"]**

In case all the PDF files you want to merge are in the same directory as that of merge.py, issue command as follow:

> **python mergepdf.py "first.pdf" "second.pdf" ["other.pdf"]**

This will generate a pdf file named "COMBINED.pdf" which will have content merged from all the pdf files mentioned in the command.

***
### Splitting files

In order to split single PDF file into a multiple files, open command prompt/terminal window and type the below command and press enter:

> **python splitpdf.py "absolute/path/to/pdffile"**

In case the PDF file you want to split are in the same directory as that of split.py, issue command as follow:

> **python splitpdf.py "first.pdf" "second.pdf" ["other.pdf"]**

This will generate multiple pdf files named "COMBINED-n.pdf" (n=1,2,3,4...) which will have page-wise content splitted from the pdf file mentioned in the command.
