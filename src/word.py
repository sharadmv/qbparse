import os

from sh import antiword
from extractor import Extractor
from docx import opendocx, getdocumenttext

class DocExtractor(Extractor):

    def __init__(self):
        pass

    def extract(self, document):
        return antiword(document)

class DocxExtractor(Extractor):

    def __init__(self):
        pass

    def extract(self, document):
        document = opendocx(document)
        textlist = getdocumenttext(document)
        return "\n".join(textlist)
