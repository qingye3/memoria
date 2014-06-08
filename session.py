# -*- coding: utf-8 -*-
from uimain import Main_Winodw
import Tkinter as tk
class Session():
    def __init__(self):
        self.word_db = None
        self.current_wordlist = None

        self.import_db_dir = None
        self.save_db_dir = None
        self.save_as_file = None
        self.open_db_dir = None
        
    def show_main_window(self):
        self.main_window = Main_Winodw(tk.Tk(), self)
        self.main_window.loop()
