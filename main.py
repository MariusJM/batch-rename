import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from os import rename
from os import startfile

class App:
    def __init__(self, master):
        self.master = master
        master.title("batch-rename")
        self.master.geometry("600x550")
        self.master.minsize(600, 550)
        self.master.pack_propagate(False)
        label_font = ("Helvetica", 10, "bold")
        background = "#e0e0e0"
        self.master.configure(bg=background)
        self.selected_files = []
        
        # top frame for file selection
        self.frame_select = tk.Frame(master, bg=background, height=60)
        self.frame_select.pack_propagate(False)

        # browse button
        self.button_browse = tk.Button(master=self.frame_select, text="Browse", command=lambda:[select_files(), preview_filenames("prefix_", "name", "_suffix")])
        
        self.button_browse.pack(side="left", padx=5,pady=5, fill="both", expand=True)

        # rename options frame
        self.frame_rename = tk.Frame(master=master, width=600, height=255, bg=background)
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

        # numeric scale
        self.frame_scale = tk.Frame(master=self.frame_rename, bg=background)
        self.scale_value = tk.DoubleVar()
        self.label_scale = tk.Label(master=self.frame_scale, text=f"Sequence number: ... _{int(self.scale_value.get())}.ext", bg=background)
        
        self.scale = tk.Scale(master=self.frame_scale, from_=1, to=6, orient="horizontal", bg=background, variable=self.scale_value, command=self.update_scale_label)

        
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

        self.label_scale.pack(padx=5, pady=5, anchor="n")

        self.frame_scale.pack(fill="x", expand=True, padx=5,pady=5)
        self.scale.pack(expand=True, fill="both", side="left", padx=5,pady=5)

        # execute buttons
        self.frame_execute = tk.Frame(master=master, width=600, height=60, bg=background)
        self.frame_execute.pack_propagate(False)

        self.button_rename = tk.Button(master=self.frame_execute, text="Rename", command=lambda:rename_files(self.entry_prefix.get(),self.entry_name.get(),self.entry_suffix.get()))
        self.button_preview = tk.Button(master=self.frame_execute, text="Preview", command=lambda:preview_filenames(self.entry_prefix.get(),self.entry_name.get(),self.entry_suffix.get()))
        self.button_quit = tk.Button(master=self.frame_execute, text="Quit", command=lambda:confirm_exit())

        self.button_rename.pack(side="left", padx=5,pady=5, fill="both", expand=True)
        self.button_preview.pack(side="left", padx=5,pady=5, fill="both", expand=True)
        self.button_quit.pack(side="left", padx=5,pady=5, fill="both", expand=True)

        # preview window
        self.frame_preview = tk.Frame(master=master, bg="#e0e0e0")
        self.frame_preview.propagate(True)
        self.label_original_name_label = tk.Label(master=self.frame_preview, text="Original file name", bg=background)
        self.label_original_name = tk.Label(master=self.frame_preview, text="file.png", bg=background)
        self.label_new_name_label = tk.Label(master=self.frame_preview, text="New file name", bg=background)
        self.label_new_name = tk.Label(master=self.frame_preview, text="prefix_file_siffix.png", bg=background)

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
            if all(value == "" for value in (prefix, name, suffix)):
                response = messagebox.askyesno("Values are empty", "Warning! Prefix, name, suffix values are empty. Are you sure you want to continue renaming?")
                if response is None:
                    return
                elif response:
                    self._execute_rename(prefix, name, suffix)

            else:
                self._execute_rename(prefix, name, suffix)

        def preview_filenames(prefix, name, suffix):
            try:
                counter = 1
                first_file = self.selected_files[0]
                original_file_name = first_file.split("/")[-1]
                extension = first_file.split(".")[-1]
                self.label_original_name.config(text=f"{original_file_name} ... + {len(self.selected_files)} more files selected")
                self.label_new_name.config(text=f"{prefix}{name}{suffix}_{str(counter).zfill(int(self.scale_value.get()))}.{extension}...{prefix}{name}{suffix}_{str(len(self.selected_files)).zfill(int(self.scale_value.get()))}.{extension}")
                print(self.selected_files)
            except IndexError:
                messagebox.showinfo("File selection", "Selec at least one file first")

        def confirm_exit():
            response = messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?")
            if response is None:
                return
            elif response:
                root.destroy()


    def _execute_rename(self, prefix, name, suffix):
        counter = 1
        try:
            for file in self.selected_files:
                file_path, file_name = file.rsplit("/", 1)
                extension = file_name.split(".")[-1]
                new_file_name = file_path + "/" + prefix + name + suffix + "_" + str(counter).zfill(int(self.scale_value.get())) + "." + extension
                print(f"file path = {file_path} | file name = {file_name} | extension = {extension} | new file name = {new_file_name}")
                rename(file, new_file_name)
                counter += 1
            startfile(file_path)
        except PermissionError:
            messagebox.showerror("Permission error", "You don't have necessary permissions to rename one or more of these files.")
        except FileExistsError:
            messagebox.showerror("File conflict", "File with specified name allready exists in this directory. Resolve the conflict and try again.")
        except FileNotFoundError:
            messagebox.showerror("File not found", "Please select the files you want to rename first.")


    def update_scale_label(self, value):
        number_to_show = str(value).zfill(int(value))
        self.label_scale.config(text=f"Sequence number: ... _{number_to_show}.ext")



    

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
