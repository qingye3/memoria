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
