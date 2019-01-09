import csv, sys


class MarkdownWriter:
    def __init__(self, fileobject):
        self.f = fileobject
        self.stdout = False

    def write(self, row):
        """ :row: a list of string"""
        line = '|' + '|'.join(row) + '|' + '\n'
        if self.stdout:
            sys.stdout.write(line)
        self.f.write(line)
        
