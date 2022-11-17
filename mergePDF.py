import PyPDF2
def merge_pdf():
    n = int(input("How many pdfs do you want to merge? "))
    pdfs = [input(f'Enter PDF {i+1} ') for i in range(0, n)]
    pdf_writer = PyPDF2.PdfFileWriter()
    for pdf in pdfs:
        f = open(pdf,'rb')
        read = PyPDF2.PdfFileReader(f)
        for p in range(read.numPages):
            page = read.getPage(p)
            pdf_writer.addPage(page)
    pdf_output = open(input("Name of merged pdf (make sure to include .pdf): "),"wb")
    pdf_writer.write(pdf_output)
    pdf_output.close()
    f.close()
merge_pdf()
