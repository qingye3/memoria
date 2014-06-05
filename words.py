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
        for line in string:
            line = line.strip()
            if line.startswith("#"):
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
                    word.definition = the_dict[word]
                except KeyError:
                    pass
                    
    def counts(self):
        return len(self.words)
        
