import os

from sh import antiword
from extractor import Extractor

class WordExtractor(Extractor):

    def __init__(self):
        pass

    def extract(self, document):
        path = document.name
        return antiword(path)
