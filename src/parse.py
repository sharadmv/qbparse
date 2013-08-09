import re
import util

from pyparsing import *
from model import *

class TossupParser:

    QUESTION_PREFIX = Regex("[0-9]+[.\)]")

    ANSWER_KEYWORD = CaselessKeyword("ANSWER")
    ANSWER_DELIMITER = Regex("[: ]")
    ANSWER_HEADER = NotAny(QuotedString("[10]"))+ANSWER_KEYWORD + ANSWER_DELIMITER
    ANSWER = ANSWER_HEADER + (SkipTo(LineEnd()) ^ SkipTo(QUESTION_PREFIX)).setResultsName("answer")

    QUESTION = Optional(ANSWER) + QUESTION_PREFIX + SkipTo(ANSWER_KEYWORD).setResultsName("question")

    TOSSUP = Forward()
    BONUS = Forward()
    TOSSUP << Group(QUESTION+ANSWER).setResultsName("tossup", listAllMatches=True) + Optional(FollowedBy(TOSSUP | BONUS))

    BONUS_POINT = Suppress("[")+Regex("[0-9]+").setResultsName("point")+Suppress("]")
    BONUS_PART = Forward()
    BONUS_ANSWER = ANSWER_HEADER+Regex(".*").setResultsName("answer")
    BONUS_PART << Group(BONUS_POINT + Regex(".*").setResultsName("question") + BONUS_ANSWER).setResultsName("bonus_part", listAllMatches=True)
    BONUS_HEADER = SkipTo(BONUS_PART).setResultsName("header")
    BONUS << Group(BONUS_HEADER + OneOrMore(BONUS_PART)).setResultsName("bonus",listAllMatches=True)

    def __init__(self):
        #self.grammar = SkipTo(self.TOSSUP).setResultsName("header")+OneOrMore(self.TOSSUP)
        self.grammar = SkipTo(self.TOSSUP) + OneOrMore(self.TOSSUP)


    def parse(self, text):
        parsed = self.grammar.parseString(text)
        tossups = []
        bonuses = []
        for tossup in parsed.tossup:
            tossups.append(Tossup(util.sanitize(tossup.question), util.sanitize(tossup.answer)))
        for bonus in parsed.bonus:
            parts = []
            for part in bonus.bonus_part:
                parts.append(BonusPart(util.sanitize(part.question), util.sanitize(part.answer), int(part.point)))
            bonuses.append(Bonus(util.sanitize(bonus.header[0]), parts))
        return {
          "tossups" : tossups,
          "bonuses" : bonuses
        }
        return parsed


if __name__ == '__main__':
    import word
    import pdf
    t = TossupParser()
    test = 'header text\nmoreheader\n1) hi\nANSWER: hi\n4. more question text\nANSWER: an answer?\n5. another question:\nANSWER: BLLHH\nThis is bonus header text\n[10] question 1\nANSWER: answer 1\n[10] Question 2:\nANSWER: answer 3\n'
    test2 = '1. This guy was awesome. \nANSWER: Sharad\n\nHeader [10] asdf asdf\nANSWER: hi\n[10] HELLO \nANSWER: sup'
    #r = t.parse(test)
    #print(r)
    #r = t.parse(test2)
    #print(r)
    doc = word.DocExtractor().extract('test/samples/msc.doc')
    docx = word.DocxExtractor().extract('test/samples/sass.docx')
    pdf = pdf.PDFExtractor().extract('test/samples/cmst.pdf')
    #print(r)
