from .NonSpaceToken import NonSapceToken


class ImplementToken(NonSapceToken):
    def test(self):
        return self.match("@implement")

class EndToken(NonSapceToken):
    def test(self):
        return self.match("@end")