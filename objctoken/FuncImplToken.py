from .NonSpaceToken import NonSapceToken

class FuncImplToken(NonSapceToken):
    def __init__(self, line):
        super().__init__(line)
        self.body = ''
        self.start = self.stop = line
        self.bracketCount = 0
        self.isBalance = False
        self.lineCount = 0

    def test(self):
        if (self.match('-') or self.match('+')):
            self.forward()
            return True
        return False

    def balanceBracket(self, line):
        for s in line:
            if s == '{':
                self.isBalance = True
                self.bracketCount = self.bracketCount + 1
            
            if s == '}':
                self.bracketCount = self.bracketCount - 1

        return self.isBalance and self.bracketCount == 0

    def append(self, line):
        self.stop = line
        self.lineCount = self.lineCount + 1
        self.body = self.body + str(line)