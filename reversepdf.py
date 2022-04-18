#!/usr/bin/python
# coding: utf-8

from Foundation import NSURL
from Quartz import PDFDocument, PDFPage
import os
import sys


def usage():
    print("Usage: {} file1.pdf … filen.pdf".format(__file__))


def main():
    print("Reversing order of pages in PDF...")

    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    for apdf in sys.argv[1:]:
        pdf_file = os.path.expanduser(apdf)
        if not pdf_file.endswith('.pdf'):
            raise Exception('PDF file type required')

        # build output PDF filename
        bpath, ext = os.path.splitext(pdf_file)
        pdfrev = os.path.basename(bpath + '_reversed' + ext)

        url = NSURL.fileURLWithPath_(pdf_file)
        pdf = PDFDocument.alloc().initWithURL_(url)
        pdf_out = PDFDocument.alloc().init()
        page_cnt = pdf.pageCount()
        pdf_page = PDFPage

        # n is sequential page increase, r is the reversed page number
        for n, r in enumerate(reversed(range(0, page_cnt))):
            pdf_page = pdf.pageAtIndex_(r)
            pdf_out.insertPage_atIndex_(pdf_page, n)

        desktop = os.path.expanduser("~/Desktop/")
        pdf_out.writeToFile_(desktop + pdfrev)

        print("PDF saved with page order reversed: " + desktop + pdfrev)


if __name__ == '__main__':
    sys.exit(main())