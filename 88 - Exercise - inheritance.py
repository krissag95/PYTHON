# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 00:11:10 2018

@author: Krisag
"""

class FileReader():
    def __init__(self, filename):
        self.filename = filename
        
    def lines(self):
        lines = []
        with open(self.filename, "r") as file:
            for line in file:
                lines.append(line.strip())
        return lines 
    
class CsvReader(FileReader):
    def __init__(self, filename):
        super().__init__(filename)
        
    def lines(self):
        lines = super().lines()
        return [line.split(",") for line in lines]
#        split_lines = []
#        for line in lines:
#            split_lines.append(line.split(","))
#        return split_lines
        
f = FileReader("./file.csv")
print(f.lines())

f = CsvReader("./file.csv")
print(f.lines())