# coding: utf-8
import sys
import difflib

class JscpdReport:

    def __init__(self):
        self.statistics = {
            "formats": { 
                "objectivec": {
                    "sources": {},
                    "total": {
                        "lines": 0,
                        "sources": 0,
                        "clones": 0,
                        "duplicatedLines": 0,
                        "percentage": 0
                    }
                }
            },
            "total": {
                "lines": 0,
                "sources": 0,
                "clones": 0,
                "duplicatedLines": 0,
                "percentage": 0
            }
        }
        self.duplicates = []

    def basename(self, path):
        return path

    def addDuplicate(self, func1, func2):
        
        firstFile = dict(
            name=self.basename(func1.path),
            start=func1.start,
            end=func1.stop
        )

        secondFile = dict(
            name=self.basename(func2.path),
            start=func2.start,
            end=func2.stop
        )

        self.duplicates.append(dict(
            format="objectivec",
            lines=func1.lineCount,
            fragment=difflib.HtmlDiff().make_table(func1.source, func2.source),
            tokens=0,
            firstFile=firstFile,
            secondFile=secondFile
        ))

        self.addStatistics(func1)
        self.addStatistics(func2)


    def addStatistics(self, func):
        key = self.basename(func.path)
        file = None
        if key in self.statistics["formats"]["objectivec"]["sources"]:
            file = self.statistics["formats"]["objectivec"]["sources"][key]
            file["clones"] = file["clones"] + 1
            file["duplicatedLines"] = file["duplicatedLines"] + func.lineCount

            self.statistics["total"]["clones"] = self.statistics["total"]["clones"] + 1

        else:
            lines = self.fileLines(func)
            file = dict(lines=lines,
                        clones=1,
                        sources=1,
                        duplicatedLines=func.lineCount)
            self.statistics["total"]["lines"] = self.statistics["total"]["lines"] + lines
            self.statistics["total"]["clones"] = self.statistics["total"]["clones"] + 1
            self.statistics["formats"]["objectivec"]["sources"][key] = file

        file["percentage"] = file["duplicatedLines"] * 100 /  file["lines"]
        self.statistics["total"]["percentage"] = self.statistics["total"]["duplicatedLines"] * 100 /  self.statistics["total"]["lines"]


    def fileLines(self, func):
        file = open(func.path, 'r')
        return len(file.readlines())


    def _asdict(self):
        return dict(statistics=self.statistics,
                    duplicates=self.duplicates)
