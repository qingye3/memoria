import Tkinter as tk
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
        self.menubar.add_cascade(label = "File", menu = file_menu)

        wordlist_menu = tk.Menu(self.menubar, tearoff = 0)
        wordlist_menu.add_command(label = "Merge", command = self._merge_cb)
        wordlist_menu.add_command(label = "Split...", command = self._split_cb)
        wordlist_menu.add_command(label = "Remove duplicates", command = self._remove_dup_cb)
        wordlist_menu.add_command(label = "Import Definition...", command = self._import_def_cb)
        wordlist_menu.add_command(label = "Randomize", command = self._randomize_cb)
        self.menubar.add_cascade(label = "Wordlist", menu = wordlist_menu)

        help_menu = tk.Menu(self.menubar, tearoff = 0)
        help_menu.add_command(label = "About...", command = self._about_cb)
        self.menubar.add_cascade(label = "Help", menu = help_menu)

    def _import_cb(self):
        commands.import_db(self.session)
        self.parent._draw()

    def _open_cb(self):
        commands.open_db(self.session)
        self.parent._draw()

    def _save_cb(self):
        commands.save_db(self.session)

    def _save_as_cb(self):
        commands.save_as_db(self.session)

    def _merge_cb(self):
        pass

    def _split_cb(self):
        pass

    def _remove_dup_cb(self):
        pass

    def _import_def_cb(self):
        pass

    def _randomize_cb(self):
        pass

    def _about_cb(self):
        pass

    def show(self):
        self.root.config(menu = self.menubar)
