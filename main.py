import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from os import rename
from os import startfile

class App:
    def __init__(self, master):
        self.master = master
        master.title("batch-rename")
        self.master.geometry("600x330")
        self.master.minsize(600, 450)
        self.master.pack_propagate(False)
        label_font = ("Helvetica", 10, "bold")
        background = "#e0e0e0"
        self.master.configure(bg=background)
        self.selected_files = []
        
        # top frame for file selection
        self.frame_select = tk.Frame(master, bg=background, height=60)
        self.frame_select.pack_propagate(False)

        # browse button
        self.button_browse = tk.Button(master=self.frame_select, text="Browse", command=lambda:select_files())
        
        self.button_browse.pack(side="left", padx=5,pady=5, fill="both", expand=True)

        # rename options frame
        self.frame_rename = tk.Frame(master=master, width=600, height=165, bg=background)
        self.frame_rename.pack_propagate(False)
        self.label_rename = tk.Label(master=self.frame_rename, text="Rename", font=label_font, bg=background)
        self.label_rename.pack(side="top", padx=1, pady=1, anchor="center")
        
        # prefix
        self.frame_prefix = tk.Frame(master=self.frame_rename, width=190, height=30, bg=background)
        self.label_prefix = tk.Label(master=self.frame_prefix, text="Prefix:", bg=background)
        self.entry_prefix = tk.Entry(master=self.frame_prefix, justify="left")



        # name
        self.frame_name = tk.Frame(master=self.frame_rename, width=190, height=30, bg=background)
        self.label_name = tk.Label(master=self.frame_name, text="Name:", bg=background)
        self.entry_name = tk.Entry(master=self.frame_name, justify="left")


        
        # suffix
        self.frame_suffix = tk.Frame(master=self.frame_rename, width=190, height=30, bg=background)
        self.label_suffix = tk.Label(master=self.frame_suffix, text="Suffix:", bg=background)
        self.entry_suffix = tk.Entry(master=self.frame_suffix, justify="left")

        self.frame_prefix.pack(fill="x", expand=True, padx=5, pady=5)
        self.label_prefix.pack(side="left", padx=5, pady=5, anchor="w")
        self.entry_prefix.pack(fill="x", expand=True)
        self.frame_name.pack(fill="x", expand=True, padx=5, pady=5)
        self.label_name.pack(side="left", padx=5, pady=5, anchor="w")
        self.entry_name.pack(fill="x", expand=True)
        self.frame_suffix.pack(fill="x", expand=True, padx=5, pady=5)
        self.label_suffix.pack(side="left", padx=5, pady=5, anchor="w")
        self.entry_suffix.pack(fill="x", expand=True)

        # execute buttons
        self.frame_execute = tk.Frame(master=master, width=600, height=60, bg=background)
        self.frame_execute.pack_propagate(False)

        self.button_rename = tk.Button(master=self.frame_execute, text="Rename", command=lambda:rename_files(self.entry_prefix.get(),self.entry_name.get(),self.entry_suffix.get()))
        self.button_preview = tk.Button(master=self.frame_execute, text="Preview", command=lambda:print_selected_files())
        self.button_quit = tk.Button(master=self.frame_execute, text="Quit", command=lambda:confirm_exit())

        self.button_rename.pack(side="left", padx=5,pady=5, fill="both", expand=True)
        self.button_preview.pack(side="left", padx=5,pady=5, fill="both", expand=True)
        self.button_quit.pack(side="left", padx=5,pady=5, fill="both", expand=True)

        # preview window
        self.frame_preview = tk.Frame(master=master, bg="#e0e0e0")
        self.frame_preview.propagate(True)
        self.label_original_name_label = tk.Label(master=self.frame_preview, text="Original file name", bg=background)
        self.label_original_name = tk.Label(master=self.frame_preview, text="file.png")
        self.label_new_name_label = tk.Label(master=self.frame_preview, text="New file name", bg=background)
        self.label_new_name = tk.Label(master=self.frame_preview, text="prefix_file_siffix.png")

        self.label_original_name_label.pack(padx=5,pady=5, anchor="w")
        self.label_original_name.pack(padx=5,pady=5, anchor="w")
        self.label_new_name_label.pack(padx=5,pady=5, anchor="w")
        self.label_new_name.pack(padx=5,pady=5, anchor="w")

        #pack frames
        self.frame_select.pack(fill="x", expand=False, padx=5,pady=5, anchor="nw")
        self.frame_rename.pack(fill="x", expand=False, padx=5,pady=5, anchor="nw")
        self.frame_execute.pack(fill="x", expand=False, padx=5,pady=5, anchor="nw")
        self.frame_preview.pack(fill="x", expand=True, padx=5,pady=5, anchor="nw")
        master.resizable(True, True)

        

        def select_files():
            filetypes = (('All files', '*.*'),('text files', '*.txt'))
            self.selected_files = list(filedialog.askopenfilenames(title='Open files', initialdir='/', filetypes=filetypes))

        def rename_files(prefix, name, suffix):
            for file in self.selected_files:
                file_path, file_name = file.rsplit("/", 1)
                extension = file_name.split(".")[-1]
                new_file_name = file_path + "/" + prefix + name + suffix + "." + extension
                print(f"file path = {file_path} | file name = {file_name} | extension = {extension} | new file name = {new_file_name}")
                rename(file, new_file_name)
            
            startfile(file_path)

        # rename(src, dst, src_dir_fd=None, dst_dir_fd=None)


        def print_selected_files():
            print(self.selected_files)

        def confirm_exit():
            response = messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?")
            if response is None:
                return
            elif response:
                root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
