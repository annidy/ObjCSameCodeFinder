class NonSapceToken:
    def __init__(self, src):
        self.src = src
        self.pos = self.fpos = 0
    
    def isSapce(self, pos):
        ch = self.src[pos]
        if ch == ' ' or ch == '\n':
            return True

        return False

    def skipSpace(self):
        pos = self.pos
        while pos < len(self.src) -1  and self.isSapce(pos):
            pos = pos + 1
        return pos

    def startswith(self, prefix, start=None):
        """判断代码是以prefix开头"""
        if start is None:
            start = self.skipSpace()

        if repr(self.src).startswith(prefix, start):
            self.fpos = start + len(prefix)
            return True

        return False

    def forward(self):
        self.pos = self.fpos
