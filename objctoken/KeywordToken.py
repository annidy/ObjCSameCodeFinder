from .NonSpaceToken import NonSapceToken


class ImplementToken(NonSapceToken):
    def test(self):
        return self.startswith("@implement")


class EndToken(NonSapceToken):
    def test(self):
        return self.startswith("@end")


class CommentsToken(NonSapceToken):
    def test(self):
        return self.startswith("//")
