import csv

class StdoutWriter:
    def write(self, row):
        """ :row: a list of string"""
        sys.stdout.write(row + '\n')


class MarkdownWriter:
    def __init__(self, fileobject):
        self.f = fileobject

    def write(self, row):
        """ :row: a list of string"""
        self.f.write('|' + '|'.join(row) + '|' + '\n')
        
