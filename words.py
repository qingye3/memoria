# -*- coding: utf-8 -*-
from pystardict import Dictionary
import random
class Word:
    def __init__(self, word = "", definition = ""):
        self.word = word 
        self.definition = definition 
    def __repr__(self):
        return "%s:\n%s"%(self.word, self.definition)

class Wordlist:
    def __init__(self):
        self.words = []

    def delete(self):
        del self.words
        self.words = []

    def append_words(self, string):
        for line in string.split('\n'):
            line = line.strip()
            if line.startswith("#"):
                continue
            self.words += [Word(word.strip()) for word in line.split(",") if word.strip()!=""]

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

    def randomize(self):
        random.shuffle(self.words)

    def __getitem__(self, n):
        return self.words[n]

    def __repr__(self):
        ret_str = ""
        for word in self.words:
            ret_str += repr(word)
            ret_str += "\n"+"-"*15+"\n"
        return ret_str

class Word_DB:
    def __init__(self, lists = []):
        if lists != [] and isinstance(lists, Wordlist):
            lists = [lists]
        self.wordlists = lists

    def append_from_file(self, file_name):
        file_in = open(file_name, 'r')
        text = ""
        for line in file_in:
            if Word_DB._is_command(line):
                if line.strip() == "@newlist":
                    new_wl = Wordlist()
                    new_wl.import_words(text) 
                    self.wordlists.append(new_wl)
                    text = ""
            else:
                text += "%s\n" %line 
        new_wl = Wordlist()
        new_wl.import_words(text) 
        self.wordlists.append(new_wl)
        file_in.close()
    def __repr__(self):
        ret_str = ""
        for i, wordlist in enumerate(self.wordlists):
            ret_str += "Wordlist %i:\n%s\n"%(i+1, "="*25)
            ret_str += repr(wordlist)
            ret_str += "*"*50 + "\n\n"
        return ret_str
    def __getitem__(self, n):
        return self.wordlists[n]
            
    @staticmethod
    def _is_command(line):
        return line.strip().startswith("@")

def merged_list(lists):
    ret_list = Wordlist()
    for l in lists:
        ret_list.words += l.words
    return ret_list 


if __name__ == "__main__":
    word_db = Word_DB()
    word_db.append_from_file("example2.txt")
    for wordlist in word_db.wordlists:
        wordlist.import_definitions("oxfordjm-ec")

    print ">>>original_db"
    print word_db

    new_list = merged_list(word_db.wordlists)
    new_list.randomize()
    new_db = Word_DB(new_list)

    word_db[0][0].definition = "changed"

    print ">>>merged and randomized"
    print new_db

    print ">>>show original one is unmodified"
    print word_db
