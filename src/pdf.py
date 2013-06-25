from pyPdf import PdfFileReader

from extractor import Extractor

class PDFExtractor(Extractor):

    def __init__(self):
        pass

    def extract(self, document):
        reader = PdfFileReader(file(document, "rb"))
        text = ""
        for page in reader.pages:
            text += page.extractText()+"\n"
        return text


