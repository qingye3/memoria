# -*- coding: utf-8 -*-
"""
This file is part of memoria
Copyright (C) 2014 Qing Ye

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from pystardict import Dictionary
import random

class Word:
    def __init__(self, word = "", definition = ""):
        self.word = word 
        self.definition = definition 
    def __repr__(self):
        if isinstance(self.word, unicode):
            word = self.word.encode("utf-8")
        else:
            word = self.word
        if isinstance(self.definition, unicode):
            definition = self.definition.encode("utf-8")
        else:
            definition = self.definition
        return "%s:\n%s"%(word, definition)

class Wordlist:
    def __init__(self, new_wordlist = []):
        self.words = new_wordlist 

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

    def __len__(self):
        return len(self.words)

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

    def __len__(self):
        return len(self.wordlists)
            
    @staticmethod
    def _is_command(line):
        return line.strip().startswith("@")

def merged_list(lists):
    ret_list = Wordlist([])
    for l in lists:
        ret_list.words += l.words
    return ret_list 

if __name__ == "__main__":
    word_db = Word_DB()
    word_db.append_from_file("example2.txt")
    for wordlist in word_db.wordlists:
        wordlist.import_definitions("/home/lh2/Workspace/memoria/oxfordjm-ec")
        #wordlist.import_definitions("oxfordjm-ec")
    import cPickle
    cPickle.dump(word_db, open("test.mem", "w"))
    a = cPickle.load(open("test.mem"))
    print a


    #new_list = merged_list(word_db.wordlists)
    #new_list.randomize()
    #new_db = Word_DB(new_list)

    #word_db[0][0].definition = "changed"

    #print ">>>merged and randomized"
    #print new_db

    #print ">>>show original one is unmodified"
    #print word_db
