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
import words
import os
import tkFileDialog
import itertools
import formats

def import_db(session):
    file_name = tkFileDialog.askopenfilename(multiple = False, initialdir = session.import_db_dir)
    if file_name == u"" or file_name == []:
        return
    session.import_db_dir = os.path.dirname(file_name)
    session.word_db = words.Word_DB()
    session.word_db.append_from_file(file_name)
    
def save_as_db(session):
    file_name = tkFileDialog.asksaveasfilename(initialdir = session.save_db_dir, defaultextension = ".xml", filetypes = [("xml memoria database", ".xml")])
    if file_name == u"" or file_name == []:
        return
    session.save_db_dir = os.path.dirname(file_name)
    session.save_as_file = file_name
    formats.save_db(session.word_db, file_name)

def save_db(session):
    if session.save_as_file == None:
        save_as_db(session)
    else:
        formats.save_db(session.word_db, file_name)

def export_as_plain(session):
    word_db = session.word_db
    file_name = tkFileDialog.asksaveasfilename(initialdir = session.export_dir, defaultextension = ".txt", filetypes = [("Plain text", ".txt")])
    if file_name:
        session.export_dir = os.path.dirname(file_name)
        file_o = open(file_name, mode = "w")
        file_o.write(repr(word_db))
        file_o.close()

def open_db(session):
    file_name = tkFileDialog.askopenfilename(multiple = False, initialdir = session.open_db_dir, filetypes = [("xml memoria database",".xml")])
    if file_name == u"" or file_name == []:
        return
    session.open_db_dir = os.path.dirname(file_name)
    session.word_db = formats.open_db(file_name)
    session.word_db.encode_utf8()

def import_definitions(session, wordlists):
    file_name = tkFileDialog.askopenfilename(multiple = False, initialdir = session.dict_dir, filetypes = [("Dictionary file", ".dict")])
    if file_name:
        session.dict_dir = os.path.dirname(file_name)
        dictionary = file_name[:-5]
        for wordlist in wordlists:
            wordlist.import_definitions(dictionary)

def randomize(session, wordlists):
    for wordlist in wordlists:
        wordlist.randomize()

def merge(session, merge_indice):
    merge_indice = list(merge_indice)
    word_db = session.word_db
    selected_wordlists = [word_db[i] for i in merge_indice]
    session.word_db.wordlists[merge_indice[0]] = words.merged_list(selected_wordlists)
    for index in reversed(merge_indice[1:]):
        del word_db.wordlists[index]

def split(session, split_indices):
    split_indices = list(split_indices)
    word_db = session.word_db
    first_index = split_indices[0]
    selected_wordlists = [word_db[i] for i in split_indices]
    merged = words.merged_list(selected_wordlists)
    for index in reversed(split_indices):
        del word_db.wordlists[index]
    num_per_list = session.num_per_list
    list_iter = _grouper(num_per_list, merged.words)
    for i,l in enumerate(list_iter):
        word_db.wordlists.insert(i+first_index,
                                words.Wordlist([x for x in l if x != None]))

def _grouper(n, iterable, fillvalue = None):
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue = fillvalue, *args)
