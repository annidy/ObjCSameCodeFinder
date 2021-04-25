# coding: utf-8

import sys
import os
import subprocess
import re


class Blamer:

    def __init__(self, path):
        self.lineDict = {}
        process = subprocess.Popen(['git', 'blame', "-w", path], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

        # Process has finished, read rest of the output 
        for output in process.stdout.readlines():
            try:
                self.parse(output)
            except:
                pass


    def parse(self, line):

        start = line.find(' ')
        recv = line[0:start]
        start = line.find('(') + 1
        end = line.find(')', start)
        data = line[start:end]


        date_start, date_end = re.search('\d{4}(.+)\d{4}', data).span()
        name = data[:date_start].strip()

        date = data[date_start:date_end]
        lineno = data[date_end:].strip()

        self.lineDict[lineno] = dict(recv=recv,
                                author=name,
                                date=date)


    def getBlame(self, line):
        return self.lineDict.get(str(line))
