# -*- coding: utf-8 -*-
import Tkinter as tk
import uimainmenu
import uicomponents
class Main_Winodw:
    def __init__(self, root, session):
        self.root = root
        self.session = session
        self._create_ui()

    def _create_ui(self):
        self._config_geometry()
        self._create_main_menu()
        self._create_wordlist_frame()
        self._create_words_frame()

    def _config_geometry(self):
        self.root.title("memoria alpha")
        self.root.geometry("600x400")

    def _create_main_menu(self):
        menubar = uimainmenu.MainMenu(self)
        menubar.show()

    def _create_wordlist_frame(self):
        frame = tk.Frame(self.root)

        buttons = tk.Frame(frame)
        merge_but = tk.Button(buttons, text = "Merge", width = 11, command = self._merge_cb)
        split_but = tk.Button(buttons, text = "Split", width = 11, command = self._split_cb)
        merge_but.pack(side = "left", fill = "x")
        split_but.pack(side = "right", fill = "x")
        buttons.pack(fill = "x", side = 'top')

        wordlists = uicomponents.ScrolledList(frame)
        wordlists.pack(fill = "both", expand = 1)
        wordlists.listbox.config(selectmode = tk.EXTENDED)
        wordlists.listbox.bind("<Double-Button-1>", self._select_wordlist_cb)

        frame.pack(fill = "y", side = 'left')

        self.wl_list = wordlists.listbox

    def _create_words_frame(self):
        frame = tk.Frame(self.root)

        toolbar = tk.Frame(frame)

        checkboxes = tk.Frame(toolbar)
        show_word_box = tk.Checkbutton(checkboxes, text = "show word")
        show_word_box.pack(side = "top")
        show_def_box = tk.Checkbutton(checkboxes, text = "show definition")
        show_def_box.pack(side = "bottom")
        checkboxes.pack(side = "left")

        buttons = tk.Frame(toolbar)
        left_but = tk.Button(buttons, text = "Previous", width = 8, command = self._left_cb)
        left_but.pack(side = "left", fill = "y")
        right_but = tk.Button(buttons, text = "Next", width = 8, command = self._right_cb)
        right_but.pack(side = "right", fill = "y")
        buttons.pack(side = "right", fill = "both")
        toolbar.pack(side = "top", expand = 1)

        wordtext = uicomponents.ScrolledText(frame)
        wordtext.text.config(height = 12)
        wordtext.pack(fill = "both")

        wordlist = uicomponents.ScrolledList(frame)
        wordlist.pack(fill = "both", expand = 1)

        frame.pack(fill = "y", side = "right", expand = 1)

        self.wordlist = wordlist.listbox
        self.wordtext = wordtext.text

    def _draw(self):
        self._draw_wordlists_db()
        self._draw_wordlist()
        self._draw_word()

    def _draw_wordlists_db(self):
        word_db = self.session.word_db
        if word_db == None:
            return
        self.wl_list.delete(0, tk.END)
        for i in range(len(word_db)):
            self.wl_list.insert(tk.END, "Wordlist %i" %(i+1))
        self.wl_list.selection_set(0)
        self.session.current_wordlist = word_db[0]
        
    def _draw_wordlist(self):
        curlist = self.session.current_wordlist
        self.wordlist.delete(0, tk.END)
        for i in range(len(curlist)):
            self.wordlist.insert(tk.END, curlist[i].word)

    def _draw_word(self):
        pass

    def _select_wordlist_cb(self, event):
        word_db = self.session.word_db
        if self.wl_list.curselection():
            items = map(int, self.wl_list.curselection())
            self.session.current_wordlist = word_db[items[0]]
            self._draw_wordlist()

    def _merge_cb(self):
        pass

    def _split_cb(self):
        pass

    def _left_cb(self):
        pass

    def _right_cb(self):
        pass

    def _show_word_cb(self):
        pass

    def _hide_word_cb(self):
        pass

    def _show_def_cb(self):
        pass

    def _hide_def_cb(self):
        pass

    def loop(self):
        self.root.mainloop()

