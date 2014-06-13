import Tkinter as tk
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
class ScrolledList(tk.Frame):
    def __init__(self, parent = None):
        tk.Frame.__init__(self, parent)
        sbar = tk.Scrollbar(self)
        list = tk.Listbox(self, relief = tk.SUNKEN)
        sbar.config(command = list.yview)
        list.config(yscrollcommand = sbar.set)
        list.config(exportselection = 0)
        sbar.pack(side = tk.RIGHT, fill = tk.Y)
        list.pack(side = tk.LEFT, expand = tk.YES, fill = tk.BOTH)
        
        self.listbox = list

class ScrolledText(tk.Frame):
    def __init__(self, parent = None):
        tk.Frame.__init__(self, parent)
        sbar = tk.Scrollbar(self)
        text = tk.Text(self, relief = tk.SUNKEN)
        sbar.config(command = text.yview)
        text.config(yscrollcommand = sbar.set)
        sbar.pack(side = tk.RIGHT, fill = tk.Y)
        text.pack(side = tk.LEFT, expand = tk.YES, fill = tk.BOTH)
        
        self.text = text 
