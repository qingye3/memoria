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
import xml.etree.ElementTree as ET
import words
def save_db(word_db, file_name):
    root = ET.Element("Database")
    for wordlist in word_db:
        wordlist_ele = ET.SubElement(root, "wordlist")
        for word in wordlist:
            word_ele = ET.SubElement(wordlist_ele, "word")
            word_text_ele = ET.SubElement(word_ele, "text")
            word_text_ele.text = word.word.decode('utf-8')
            word_def_ele = ET.SubElement(word_ele, "definition")
            word_def_ele.text = word.definition.decode('utf-8')
    ET.ElementTree(root).write(file_name, encoding = "UTF-8")

def open_db(file_name):
    root = ET.parse(file_name).getroot()
    new_db_list = []
    for wordlist in root.findall('wordlist'):
        new_word_list = []
        for word in wordlist.findall('word'):
            text = word.find('text').text
            definition = word.find('definition').text
            new_word = words.Word(text, definition)
            new_word_list.append(new_word)
        new_db_list.append(words.Wordlist(new_word_list))
    word_db = words.Word_DB(new_db_list)
    return word_db
        
