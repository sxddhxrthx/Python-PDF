#mergepdf

import PyPDF2
import sys

inputs = sys.argv[1:]

def mergepdf(pdf_list):
	merger_object = PyPDF2.PdfMerger()
	for pdf in pdf_list:
		print(pdf)
		merger_object.append(pdf)
	merger_object.write('COMBINED.pdf')
	
	
mergepdf(inputs)
