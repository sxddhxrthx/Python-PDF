# code to split pdf 

#this change should reflect in main branch

from PyPDF2 import PdfFileWriter, PdfFileReader
import os, sys


def split_pdf(path):
	fname = os.path.splitext(os.path.basename(path))[0]
	
	pdf = PdfFileReader(path)
	for page in range(pdf.getNumPages()):
		writer_object = PdfFileWriter()
		writer_object.addPage(pdf.getPage(page))
		
		output_pdf = '{}_page_{}.pdf'.format(fname, page+1)
		with open(output_pdf, 'wb') as opt:
			writer_object.write(opt)
		print('PDF Split complete')
		
if __name__ == '__main__':
	inputs = sys.argv[1]
	split_pdf(inputs)