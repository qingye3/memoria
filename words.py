# -*- coding: utf-8 -*-
from pystardict import Dictionary
class Word:
    def __init__(self, word = "", definition = ""):
        self.word = word 
        self.definition = definition 
        self.proficiency = 0.0

class Wordlist:
    def __init__(self):
        self.words = []

    def delete(self):
        del self.words
        self.words = []

    def append_words(self, string):
        for line in string.split('\n'):
            line = line.strip()
            if line.startswith("#")\
            or line == "":
                continue
            self.words += [Word(word.strip()) for word in line.split(",")]

    def import_words(self, string):
        self.delete()
        self.append_words(string)

    def import_definitions(self, dictionary):
        the_dict = Dictionary(dictionary) 
        for word in self.words:
            if word.definition == "":
                try:
                    word.definition = the_dict[word.word]
                except KeyError:
                    pass
                    
    def counts(self):
        return len(self.words)
        
#test
if __name__ == "__main__":
    wl = Wordlist()
    text = open("example.txt").read()
    wl.append_words(text)
    wl.import_definitions("oxfordjm-ec")
    for word in wl.words:
        print word.word,":"
        print word.definition
        print "="*15
