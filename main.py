import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        master.title("batch-rename")
        self.master.geometry("600x330")
        self.master.pack_propagate(False)
        label_font = ("Helvetica", 10, "bold")
        background = "#e0e0e0"

        # top frame for file selection
        self.frame_select = tk.Frame(master, width=600, height=40, bg=background)
        self.frame_select.pack_propagate(False)

        # browse button
        self.button_browse = tk.Button(master=self.frame_select, width=200, height=40, text="Browse")
        
        self.button_browse.pack(anchor="n", padx=5, pady=5)

        # rename options frame
        self.frame_rename = tk.Frame(master=master, width=600, height=65, bg=background)
        self.frame_rename.pack_propagate(False)
        self.label_rename = tk.Label(master=self.frame_rename, text="Rename", font=label_font, bg=background)
        # self.label_rename.place(relx=0.5, rely=0.5, anchor="center")
        self.label_rename.pack(side="top", padx=1, pady=1, anchor="center")
        
        # prefix
        self.frame_prefix = tk.Frame(master=self.frame_rename, width=190, height=30, bg=background)
        self.label_prefix = tk.Label(master=self.frame_prefix, text="Prefix:")
        self.entry_prefix = tk.Entry(master=self.frame_prefix, justify="left")

        self.frame_prefix.pack(side="left", padx=5, pady=5)
        self.label_prefix.pack(side="left", padx=5, pady=5, anchor="w")
        self.entry_prefix.pack(fill="x", expand=True)

        # name
        self.frame_name = tk.Frame(master=self.frame_rename, width=190, height=30, bg=background)
        self.label_name = tk.Label(master=self.frame_name, text="Name:")
        self.entry_name = tk.Entry(master=self.frame_name, justify="left")

        self.frame_name.pack(side="left", padx=5, pady=5)
        self.label_name.pack(side="left", padx=5, pady=5, anchor="w")
        self.entry_name.pack(fill="x", expand=True)
        
        # suffix
        self.frame_suffix = tk.Frame(master=self.frame_rename, width=190, height=30, bg=background)
        self.label_suffix = tk.Label(master=self.frame_suffix, text="Suffix:")
        self.entry_suffix = tk.Entry(master=self.frame_suffix, justify="left")

        self.frame_suffix.pack(side="left", padx=5, pady=5)
        self.label_suffix.pack(side="left", padx=5, pady=5, anchor="w")
        self.entry_suffix.pack(fill="x", expand=True)

        # execute buttons
        self.frame_execute = tk.Frame(master=master, width=600, height=60, bg=background)
        self.frame_execute.pack_propagate(False)
        self.button_rename = tk.Button(master=self.frame_execute, text="Rename")
        self.button_preview = tk.Button(master=self.frame_execute, text="Preview")
        self.button_quit = tk.Button(master=self.frame_execute, text="Quit")

        self.button_rename.pack(side="left", padx=5,pady=5, fill="both", expand=True)
        self.button_preview.pack(side="left", padx=5,pady=5, fill="both", expand=True)
        self.button_quit.pack(side="left", padx=5,pady=5, fill="both", expand=True)



        # preview window
        self.frame_preview = tk.Frame(master=master, width=600, height=60, bg="#e0e0e0")
        self.label_original_name_label = tk.Label(master=self.frame_preview, text="Original file name")
        self.label_original_name = tk.Label(master=self.frame_preview, text="file.png")
        self.label_new_name_label = tk.Label(master=self.frame_preview, text="New file name")
        self.label_new_name = tk.Label(master=self.frame_preview, text="prefix_file_siffix.png")

        self.label_original_name_label.pack(padx=5,pady=5, anchor="w")
        self.label_original_name.pack(padx=5,pady=5, anchor="w")
        self.label_new_name_label.pack(padx=5,pady=5, anchor="w")
        self.label_new_name.pack(padx=5,pady=5, anchor="w")

        #pack frames
        self.frame_select.pack(expand=False, padx=5,pady=5, anchor="w")
        self.frame_rename.pack(expand=False, padx=5,pady=5, anchor="w")
        self.frame_execute.pack(expand=False, padx=5,pady=5, anchor="w")
        self.frame_preview.pack(expand=False, padx=5,pady=5, anchor="w")
        master.resizable(False, False)



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
