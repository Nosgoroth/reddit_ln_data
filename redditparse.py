import os, sys, json, re, datetime
from collections import Counter
from pprint import pprint

def normalize(s):
    return s.strip().lower()

def removeMarkdownLink(s):
    return re.sub(r"\[(.+)\]\(.+\)", r"\1", s)

class LightNovelVolume:
    date = None
    series = None
    volume = None
    publisher = None
    release = None

    isPhysical = False
    isDigital = False

    def __init__(self, rawline, year):
        parts = rawline.split('|')
        self.date = "%s, %s" % (normalize(parts[0]), year)
        self.series = removeMarkdownLink(normalize(parts[1]))
        self.volume = normalize(parts[2])
        self.publisher = removeMarkdownLink(normalize(parts[3]))
        self.release = normalize(parts[4])
        self.isPhysical = ('physical' in self.release)
        self.isDigital = ('digital' in self.release)

def parseFile(filename, year):
    items = []
    with open(filename) as f:
        for line in f:
            items.append(LightNovelVolume(line, year))
    return items

if __name__ == "__main__":
    
    items = parseFile('redditraw_2020.md', 2020)
    items += parseFile('redditraw_2019.md', 2019)
    
    print()
    print("Types of release:")
    pprint(Counter([x.release for x in items]))
    
    # Filter only digital
    items = [x for x in items if x.isDigital]

    print()
    print("Releases per publisher:")
    pprint(Counter([x.publisher for x in items]))

    # Do more stuff here
    # xx = ["%s %s (%s)" % (x.series, x.volume, x.date) for x in items if x.publisher == 'sol press']
    # for x in xx: print(x)
