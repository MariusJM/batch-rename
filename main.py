import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        master.title("batch-rename")
        # self.master.geometry("600x300")
        self.master.pack_propagate(True)
        # top frame for file selection
        self.frame_select = tk.Frame(master, width=500, height=30, bg="#e0e0e0")
        self.frame_select.pack_propagate(True)
        self.button_browse = tk.Button(master=self.frame_select, text="Browse")
        self.button_browse.pack(padx=5, pady=5)

        # rename options frame
        self.frame_rename = tk.Frame(master, width=500, height=60, bg="#e0e0e0")
        self.frame_rename.pack_propagate(True)
        
        self.label_rename = tk.Label(master=self.frame_rename, text="Rename")
        self.label_rename.pack(side="top", padx=2, pady=2, anchor="w")  # Set anchor to "west" (left)
        
        # prefix
        self.frame_prefix = tk.Frame(master=self.frame_rename, width=200, height=30, bg="#e0e0e0")
        self.frame_prefix.pack(side="left", padx=5, pady=5)
        self.label_prefix = tk.Label(master=self.frame_prefix, text="Prefix:")
        self.label_prefix.pack(side="left", padx=5, pady=5, anchor="w")  # Set anchor to "west" (left)
        self.entry_prefix = tk.Entry(master=self.frame_prefix, justify="left")
        self.entry_prefix.pack(padx=5, pady=5)

        # name
        self.frame_name = tk.Frame(master=self.frame_rename, width=200, height=30, bg="#e0e0e0")
        self.frame_name.pack(side="left", padx=5, pady=5)
        self.label_name = tk.Label(master=self.frame_name, text="Name:")
        self.label_name.pack(side="left", padx=5, pady=5, anchor="w")  # Set anchor to "west" (left)
        self.entry_name = tk.Entry(master=self.frame_name, justify="left")
        self.entry_name.pack(padx=5, pady=5)
        
        # suffix
        self.frame_suffix = tk.Frame(master=self.frame_rename, width=200, height=30, bg="#e0e0e0")
        self.frame_suffix.pack(side="left", padx=5, pady=5)
        self.label_suffix = tk.Label(master=self.frame_suffix, text="Suffix:")
        self.label_suffix.pack(side="left", padx=5, pady=5, anchor="w")  # Set anchor to "west" (left)
        self.entry_suffix = tk.Entry(master=self.frame_suffix, justify="left")
        self.entry_suffix.pack(padx=5, pady=5)

        #pack frames
        self.frame_select.pack(padx=5,pady=5)
        self.frame_rename.pack(padx=2,pady=2)
        master.resizable(False, False)

    def on_button_click(self):
        name = self.entry.get()
        self.label.config(text="Hello, " + name)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
