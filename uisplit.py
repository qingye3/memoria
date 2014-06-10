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
        
    
