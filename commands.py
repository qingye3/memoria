# -*- coding: utf-8 -*-
import words
import os
import tkFileDialog
import cPickle

def import_db(session):
    file_name = tkFileDialog.askopenfilename(multiple = False, initialdir = session.import_db_dir)
    if file_name == u"" or file_name == []:
        return
    session.import_db_dir = os.path.dirname(file_name)
    session.word_db = words.Word_DB()
    session.word_db.append_from_file(file_name)
    
def save_as_db(session):
    file_name = tkFileDialog.asksaveasfilename(initialdir = session.import_db_dir, defaultextension = ".mem", filetypes = [("memoria file", ".mem")])
    if file_name == u"" or file_name == []:
        return
    session.save_db_dir = os.path.dirname(file_name)
    session.save_as_file = file_name
    file_o = open(file_name, "w")
    cPickle.dump(obj = session.word_db, file = file_o, protocol = 2)
    file_o.close()

def save_db(session):
    if session.save_as_file == None:
        save_as_db(session)
    else:
        file_o = open(session.save_as_file, "w")
        cPickle.dump(obj = session.word_db, file = file_o, protocol = 2)
        file_o.close()

def open_db(session):
    file_name = tkFileDialog.askopenfilename(multiple = False, initialdir = session.open_db_dir, filetypes = [("memoria file",".mem")])
    if file_name == u"" or file_name == []:
        return
    session.open_db_dir = os.path.dirname(file_name)
    file_in = open(file_name, "r")
    session.word_db = cPickle.load(file_in)
    file_in.close()

    
