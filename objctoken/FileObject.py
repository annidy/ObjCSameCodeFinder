class LineString:
    def __init__(self, str, lineno: int):
        '''初始化。lineno 行号'''
        self.str = str
        self.lineno = lineno

    def __iter__(self):
        return self.str.__iter__()

    def __getitem__(self, subscript):
        return self.str.__getitem__(subscript)

    def __repr__(self) -> str:
        return self.str + ', <' + str(self.lineno) + '>'

    def __str__(self) -> str:
        return self.str.__str__()

    def __len__(self):
        return self.str.__len__()

    def to_json(self):
        return self.str   
        
class FileObject:
    def __init__(self, path):
        self.path = path
        with open(path) as f:
            self.lines = f.readlines()
        self.iteri = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            line = LineString(self.lines[self.iteri], lineno=self.iteri+1)
        except IndexError:
            raise StopIteration

        self.iteri = self.iteri + 1
        return line

