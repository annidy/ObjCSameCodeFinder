

class NonSapceToken:
    def __init__(self, src):
        self.src = src
        self.pos = 0
        pass
    
    def isSapce(self):
        ch = self.src[self.pos]
        if ch == ' ' or ch == '\n':
            return True

        return False

    def skipSpace(self):
        while self.isSapce():
            self.pos = self.pos + 1
            if self.pos >= len(self.src):
                self.pos = len(self.src) - 1
                return None 
            
        return self.src[self.pos]

    def match(self, src):
        self.skipSpace()
        if self.src[self.pos:].startswith(src):
            self.fpos = self.pos + len(src)
            return True
        return False

    def forward(self):
        self.pos = self.fpos
