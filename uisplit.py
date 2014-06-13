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
import commands
class Split_Window():
    def __init__(self, parent):
        self.parent = parent
        self.session = parent.session
        self.top = tk.Toplevel(parent.root)
        tk.Label(self.top, text = "Number per list:").pack()
        self.entry = tk.Entry(self.top)
        self.entry.insert(0, str(self.session.num_per_list))
        self.entry.pack()
        tk.Button(self.top, text = "Confirm", command = self._confirm).pack()

    def _confirm(self):
        self.session.num_per_list = int(self.entry.get())
        selected_indices = self.parent.wl_list.curselection() 
        commands.split(self.session, selected_indices)
        self.parent._draw()
        
    
