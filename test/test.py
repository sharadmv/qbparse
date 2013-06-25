import sys, os, unittest
sys.path.insert(0, os.path.dirname("../src/"))

from parse import *

class TossupParsingTest(unittest.TestCase):
    def setUp(self):
        self.parser = TossupParser()
        self.simple = open('samples/tossups.txt').read()
        self.lines = open('samples/tossups_linebreak.txt').read()
        self.lines2 = open('samples/tossups_linebreak2.txt').read()
        self.tb = open('samples/tb.txt').read()

    def testSanity(self):
        parsed = self.parser.parse(self.simple)
        assert len(parsed['tossups']) == 2, "Incorrect number of tossups extracted"
        tossups = parsed['tossups']
        assert tossups[0].answer == "Sharad Vikram", "Incorrect answer parsed"
        assert tossups[1].answer == "Sharad Vikram", "Incorrect answer parsed"
        assert tossups[0].question == "This guy did nothing really", "Incorrect question parsed"
        assert tossups[1].question == "This person also did nothing", "Incorrect question parsed"

    def testLineBreak(self):
        parsed = self.parser.parse(self.lines)
        assert len(parsed['tossups']) == 2, "Incorrect number of tossups extracted"
        tossups = parsed['tossups']
        assert tossups[0].answer == "Sharad Vikram", "Incorrect answer parsed"
        assert tossups[1].answer == "Sharad Vikram", "Incorrect answer parsed"
        assert tossups[0].question == "This guy did nothing really", "Incorrect question parsed"
        assert tossups[1].question == "This person also did nothing", "Incorrect question parsed"

    def testLineBreak2(self):
        parsed = self.parser.parse(self.lines2)
        assert len(parsed['tossups']) == 2, "Incorrect number of tossups extracted"
        tossups = parsed['tossups']
        assert tossups[0].answer == "Sharad Vikram", "Incorrect answer parsed"
        assert tossups[1].answer == "Sharad Vikram", "Incorrect answer parsed"
        assert tossups[0].question == "This guy did nothing really", "Incorrect question parsed"
        assert tossups[1].question == "This person also did nothing", "Incorrect question parsed"


    def testTossupBonuses(self):
        parsed = self.parser.parse(self.tb)
        assert len(parsed['tossups']) == 2, "Incorrect number of tossups extracted"
        tossups = parsed['tossups']
        assert tossups[0].answer == "Sharad Vikram", "Incorrect answer parsed"
        assert tossups[1].answer == "Sharad Vikram", "Incorrect answer parsed"
        assert tossups[0].question == "This guy did nothing really", "Incorrect question parsed"
        assert tossups[1].question == "This person also did nothing", "Incorrect question parsed"

if __name__ == "__main__":
    unittest.main()
