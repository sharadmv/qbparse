class Tossup:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return self.question+"\nANSWER: "+self.answer

    def __repr__(self):
        return self.__str__()

class Bonus:
    def __init__(self, header, parts):
        self.header = header
        self.parts = parts

class BonusPart:
    def __init__(self, question, answer, points):
        self.question = question
        self.answer = answer
        self.points = points

