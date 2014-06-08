import Tkinter as tk
class ScrolledList(tk.Frame):
    def __init__(self, parent = None):
        tk.Frame.__init__(self, parent)
        sbar = tk.Scrollbar(self)
        list = tk.Listbox(self, relief = tk.SUNKEN)
        sbar.config(command = list.yview)
        list.config(yscrollcommand = sbar.set)
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
