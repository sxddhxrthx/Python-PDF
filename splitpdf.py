#split pdf

from PyPDF2 import PdfWriter, PdfReader
import os, sys


def split_pdf(path):
	fname = os.path.splitext(os.path.basename(path))[0]
	
	pdf = PdfReader(path)
	for page in range(len(pdf.pages)):
		writer_object = PdfWriter()
		writer_object.add_page(pdf.pages[page])
		
		output_pdf = '{}_page_{}.pdf'.format(fname, page+1)
		with open(output_pdf, 'wb') as opt:
			writer_object.write(opt)
		print('PDF Split complete')
		
if __name__ == '__main__':
	inputs = sys.argv[1]
	split_pdf(inputs)
