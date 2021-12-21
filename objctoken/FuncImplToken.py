from .NonSpaceToken import NonSapceToken
from .KeywordToken import CommentsToken


class FuncImplToken(NonSapceToken):
    def __init__(self, line):
        super().__init__(line)
        self.body = ''
        self.start = self.stop = line
        self.bracketCount = 0
        self.isBalance = False
        self.lineCount = 0

    def test(self):
        if (self.startswith('-') or self.startswith('+')):
            self.forward()
            return True
        return False

    def balanceBracket(self, line):
        # 过滤注释
        token = CommentsToken(line)
        if token.test():
            return False

        for s in line:
            # FIXME: 需要处理注释、字符串等特殊情况
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
