# -*- coding: utf-8 -*-
"""
This is part of memoria
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
from uimain import Main_Winodw
import Tkinter as tk
class Session():
    def __init__(self):
        self.word_db = None
        self.current_wordlist = None
        self.current_word = None

        self.import_db_dir = None
        self.save_db_dir = None
        self.save_as_file = None
        self.open_db_dir = None
        self.dict_dir = None
        self.export_dir = None

        self.num_per_list = 5
        
    def show_main_window(self):
        self.main_window = Main_Winodw(tk.Tk(), self)
        self.main_window.loop()
