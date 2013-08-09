import sh
import os

from sh import pdftotext

from extractor import Extractor

class PDFExtractor(Extractor):

    def __init__(self):
        pass

    def extract(self, document):
        return pdftotext(document, "-").encode('utf-8', 'ignore')


