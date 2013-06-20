from pdfminer.pdfinterp import process_pdf, PDFResourceManager
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from cStringIO import StringIO

from extractor import Extractor

class PDFExtractor(Extractor):

    def __init__(self):
        self.rm = PDFResourceManager()
        self.codec = 'utf-8'
        self.params = LAParams()

    def extract(self, document):
        string = StringIO()
        device = TextConverter(self.rm, string, codec=self.codec, laparams=self.params)
        process_pdf(self.rm, device, document)
        document.close()
        device.close()
        text = string.getvalue()
        string.close()
        return text


