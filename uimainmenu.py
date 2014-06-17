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
import Tkinter as tk
import uisplit
import uiedit
import commands
class MainMenu:
    def __init__(self, parent):
        self.parent = parent
        self.root = parent.root
        self.session = parent.session
        self._create_menu()

    def _create_menu(self):
        self.menubar = tk.Menu(self.root)

        file_menu = tk.Menu(self.menubar, tearoff = 0)
        file_menu.add_command(label = "Import...", command = self._import_cb)
        file_menu.add_command(label = "Open... ", command = self._open_cb) 
        file_menu.add_command(label = "Save... ", command = self._save_cb)
        file_menu.add_command(label = "Save as...", command = self._save_as_cb)
        file_menu.add_command(label = "Export as plain text...", command = self._export_plain_cb)
        self.menubar.add_cascade(label = "File", menu = file_menu)

        wordlist_menu = tk.Menu(self.menubar, tearoff = 0)
        wordlist_menu.add_command(label = "Edit...", command = self._edit_cb)
        wordlist_menu.add_command(label = "Merge", command = self._merge_cb)
        wordlist_menu.add_command(label = "Split...", command = self._split_cb)
        #wordlist_menu.add_command(label = "Remove duplicates", command = self._remove_dup_cb)
        wordlist_menu.add_command(label = "Import Definition...", command = self._import_def_cb)
        wordlist_menu.add_command(label = "Randomize", command = self._randomize_cb)
        self.menubar.add_cascade(label = "Wordlist", menu = wordlist_menu)

        #help_menu = tk.Menu(self.menubar, tearoff = 0)
        #help_menu.add_command(label = "About...", command = self._about_cb)
        #self.menubar.add_cascade(label = "Help", menu = help_menu)

    def _import_cb(self):
        commands.import_db(self.session)
        self.parent._draw()

    def _open_cb(self):
        commands.open_db(self.session)
        self.parent._draw()

    def _save_cb(self):
        commands.save_db(self.session)

    def _export_plain_cb(self):
        commands.export_as_plain(self.session)

    def _save_as_cb(self):
        commands.save_as_db(self.session)

    def _edit_cb(self):
        edit_window = uiedit.Edit_Window(self.parent)

    def _merge_cb(self):
        merge_indice= self.parent.wl_list.curselection() 
        commands.merge(self.session, merge_indice)
        self.parent._draw()

    def _split_cb(self):
        split_window = uisplit.Split_Window(self.parent)

    def _remove_dup_cb(self):
        pass

    def _import_def_cb(self):
        selected_indices = self.parent.wl_list.curselection() 
        word_db = self.session.word_db
        selected_wordlists = [word_db[i] for i in selected_indices]
        commands.import_definitions(self.session, selected_wordlists)
        self.parent._draw_word()

    def _randomize_cb(self):
        selected_indices = self.parent.wl_list.curselection() 
        word_db = self.session.word_db
        selected_wordlists = [word_db[i] for i in selected_indices]
        commands.randomize(self.session, selected_wordlists)
        self.parent._draw_wordlist()

    def _about_cb(self):
        pass

    def show(self):
        self.root.config(menu = self.menubar)
