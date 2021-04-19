# coding: utf-8
import re
from simhash import Simhash, SimhashIndex

def get_features(s):
    width = 3
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

class FuncHash:

    def __init__(self, dict):
        super().__init__()
        self.path = dict.get("path")
        self.start = dict.get("start")
        self.stop = dict.get("stop")
        self.source = dict.get("source")
        self.lineCount = len(self.source.split('\n'))

    def hashSource(self):
        self.simHash = Simhash(get_features(self.source))

    def distance(self, to):
        return self.simHash.distance(to.simHash)

    def _asdict(self):
        return dict(path=self.path,
                    start=self.start,
                    stop=self.stop,
                    source=self.source)