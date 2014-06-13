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
import words
class Edit_Window():
    def __init__(self, parent):
        self.parent = parent
        self.session = parent.session
        self.top = tk.Toplevel(parent.root)

        tk.Label(self.top, text = "Word").pack()
        self.word_entry = tk.Entry(self.top, width = 25)
        self.word_entry.pack()

        tk.Label(self.top, text = "Definition").pack()
        self.definition_text = tk.Text(self.top, width = 25, height = 5)
        self.definition_text.pack()

        self.confirm_but = tk.Button(self.top, text = "Confirm", command = self.confirm)
        self.confirm_but.pack()

        self.update()

    def update(self):
        word = self.session.current_word
        self.word_entry.delete(0, tk.END)
        self.word_entry.insert(0, word.word)

        self.definition_text.delete(1.0, tk.END)
        self.definition_text.insert(tk.END, word.definition)

    def confirm(self):
        word = self.session.current_word
        word.word = self.word_entry.get()
        word.definition = self.definition_text.get(1.0, tk.END)
        self.parent._draw_word()
        self.top.destroy()
