# coding: utf-8
import re
from simhash import Simhash, SimhashIndex

class FuncHash:

    def __init__(self, dict):
        super().__init__()
        self.path = dict.get("path")
        self.start = dict.get("start")
        self.stop = dict.get("stop")
        self.source = dict.get("source")
        self.startLoc = dict.get("startLoc")
        self.stopLoc = dict.get("stopLoc")
        self.lineCount = len(self.source.split('\n'))

    def hashSource(self):
        self.simHash = Simhash(self.source)

    def distance(self, to):
        return self.simHash.distance(to.simHash)

    def _asdict(self):
        return dict(path=self.path,
                    start=self.start,
                    stop=self.stop,
                    source=self.source)