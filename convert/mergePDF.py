#!/usr/bin/env python

from PyPDF2 import PdfFileReader, PdfFileWriter
#import pikepdf

def remove_page(path, output, page_to_Remove):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(path)
    idx = 1
    for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            if(idx!=page_to_Remove):
                print("Adding Page: "+str(idx))
                pdf_writer.addPage(pdf_reader.getPage(page))
            idx = idx+1
    
    with open(output, 'wb') as out:
        pdf_writer.write(out)


def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)        
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object            
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    # txt = f"""
    # Information about {pdf_path}: 

    # Author: {information.author}
    # Creator: {information.creator}
    # Producer: {information.producer}
    # Subject: {information.subject}
    # Title: {information.title}
    # Number of pages: {number_of_pages}
    # """

    print(txt)
    return information

def decrypt_pdf(input_path, output_path, password):
  with open(input_path, 'rb') as input_file, \
    open(output_path, 'wb') as output_file:
    reader = PdfFileReader(input_file)
    reader.decrypt(password)

    writer = PdfFileWriter()

    for i in range(reader.getNumPages()):
      writer.addPage(reader.getPage(i))

    writer.write(output_file)

def decrypt_pdf2(input_path, output_path, password):
    with pikepdf.open(input_path, password) as pdf:
        num_pages = len(pdf.pages)
        print("Total pages:", num_pages)

if __name__ == '__main__':
    doc_1 = '/Users/anshul/Documents/docs/E-Aadhar-password-ANSH1981.pdf'
    doc_2 = '/Users/anshul/Documents/docs/E-Aadhar-password-ANSH1981-dec.pdf'
    # doc_3 = '/Users/anshul/Downloads/Shruti-Quantum-9991336776.pdf'
    # doc_4 = '/Users/anshul/Downloads/Shruti-Quantum-9991353164.pdf'
    # doc_5 = '/Users/anshul/Downloads/page-05.pdf'    
    # doc_6 = '/Users/anshul/Downloads/page-06.pdf'    
    # doc_7 = '/Users/anshul/Downloads/page-07.pdf'    
    # doc_8 = '/Users/anshul/Downloads/page-08.pdf'    
    # doc_9 = '/Users/anshul/Downloads/page-09.pdf'    
    # doc_10 = '/Users/anshul/Downloads/page-10.pdf'    

    #extract_information('/Users/anshul/Downloads/abc.pdf')
    # paths = [doc_1, doc_2, doc_3, doc_4, doc_5, doc_6, doc_7, doc_8, doc_9, doc_10 ]
    # paths = [doc_1, doc_2, doc_3]
    # merge_pdfs(paths, output='/Users/anshul/Downloads/life-certificate-2021.pdf')
    # remove_page(doc_1,doc_2,2)
    # encrypted = '/Users/anshul/Downloads/ELSS-Statement-encrypted.pdf'
    # decrypted = '/Users/anshul/Downloads/ELSS-Statement.pdf'
    # password = 'AMYPK6172H'
    decrypt_pdf(doc_1, doc_2, "ANSH1981")
    # decrypt_pdf(doc_2, doc_4, "BLXPS4482F")
