# NITROGEN: Install Oxygen and run it.
# Download this file and run it. And Oxygen will install!

import os
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from pathlib import Path
import sys
import io
import tkinter.messagebox
import urllib.request


def texteditor():
    os.chdir(os.getcwd() + "/oxygen/workspace")
    def open_file():
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("Oxygen Files", "*.oxy"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        txt_edit.delete(1.0, END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(END, text)
        window.title(f"Nitrogen - {filepath}")

    def save_file():
        """Save the current file as a new file."""
        filepath = asksaveasfilename(
            defaultextension=".oxy",
            filetypes=[("Oxygen Files", "*.oxy"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = txt_edit.get(1.0, END)
            output_file.write(text)
        window.title(f"Nitrogen - {filepath}")

    class add_path():
        def __init__(self, path):
            self.path = path

        def __enter__(self):
            sys.path.insert(0, self.path)

        def __exit__(self, exc_type, exc_value, traceback):
            try:
                sys.path.remove(self.path)
            except ValueError:
                pass

    
    def run_file():
        input = txt_edit.get("1.0",END)
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        with add_path(sys.path[0] + "/oxygen"):
            from oxygen import Oxygen
            oxygen = Oxygen("\n" + input + "\n")
            result = oxygen.lexer()
            if result["error"] != False:
                print("Lexer: " + result["error"])
                sys.exit()
            oxygen.parse(result["tokens"])
        sys.stdout = old_stdout
        whatWasPrinted = buffer.getvalue()
        tkinter.messagebox.showinfo("Nitrogen - Result",  whatWasPrinted)
        
        buffer.close()
    
    window = Tk()
    window.title("Nitrogen")
    window.resizable(0, 0)
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)

    txt_edit = Text(window) 
    fr_buttons = Frame(window, relief=RAISED)
    btn_open = Button(fr_buttons, text="Open", command=open_file)
    btn_save = Button(fr_buttons, text="Save As...", command=save_file)
    btn_run = Button(fr_buttons, text="Run", command=run_file)

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
    btn_run.grid(row=2, column=0, sticky="ew", padx=5)
    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")

    window.mainloop()
    
    
    


output = os.system("cd oxygen  >/dev/null 2>&1")

if output == 0:
    texteditor()
else:
    def loadinstall():
        def startnitrogenfrominstall():
            root1.destroy()
            os.execl(sys.executable, sys.executable, *sys.argv)
        root.destroy()
        root1 = Tk()
        root1.title("Install")
        root1.geometry('600x600')
        textbar = Label(root1, text="Starting")
        textbar.pack()
        progress = Progressbar(root1, orient = HORIZONTAL,
              length = 100, mode = 'determinate')
        progress.pack(pady = 10)
        progress['value'] = 20
        textbar.config(text='Downloading Oxygen from GitHub')
        root1.update_idletasks()
        os.system("git clone https://github.com/arjunj132/oxygen.git")
        page = urllib.request.urlopen('https://raw.githubusercontent.com/arjunj132/oxygen/ntirogen/oxygen.py')
        h = open("oxygen/oxygen.py", "w")
        h.write(page.read().decode("utf-8"))
        h.close()
        textbar.config(text='Creating bash files...')
        progress['value'] = 40
        root1.update_idletasks()
        g = open("nitrogen.sh", "w")
        g.write("# This file is neccacary for Nitrogen to work")
        os.system("bash nitrogen.sh")
        progress["value"] = 60
        textbar.config(text='Testing...')
        root1.update_idletasks()
        from oxygen.oxygen import Oxygen
        oxygen = Oxygen("\n" + "print \"Test\"" + "\n")
        result = oxygen.lexer()
        if result["error"] != False:
            Label(root1, text="Error: " + result["error"])
        else:
            print("Tested successfully")
        progress["value"] = 80
        textbar.config(text='Setting up text editor...')
        root1.update_idletasks()
        print("Check wiki to learn more: https://github.com/arjunj132/oxygen/wiki")
        Path("oxygen/workspace").mkdir(parents=True, exist_ok=True)
        progress["value"] = 100
        textbar.config(text='Done installing Oxygen')
        Button(root1, text="Start Nitrogen Editor", command=startnitrogenfrominstall).pack()
        root1.update_idletasks()
        root1.mainloop()
        
    root = Tk()
    root.title("Install - Terms")
    root.geometry('600x600')
    Label(root, text="Welcome to Nitrogen, the reccomended way to install Oxygen.").pack()
    Label(root, text="Please read the following information.").pack()
    message ='''Introdution:     
Hello! You are installing a fresh new copy of the Oxygen Programming Language. Plese read the text below and agree to install Oxygen.


What's new:
The OPL and the first version of Oxygen is released.



How to use:
Just use Nitrogen editor to run the Oxygen files. Or use command line:
python3 -m runfile file.oxy



License:

MIT License

Copyright (c) 2022 arjunj132

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

    f = Frame(root)
    f.pack()

    text_box = Text(
        f,
        height=20,
        width=40
    )
    text_box.pack(side="left")
    text_box.insert('end', message)
    text_box.config(state='disabled')
    scrollb = Scrollbar(f, command=text_box.yview)
    scrollb.pack(side=RIGHT, fill=Y)
    text_box['yscrollcommand'] = scrollb.set
    Label(root, text="").pack()
    agree = Button(root, text="Agree", command=loadinstall)
    agree.pack()
    root.mainloop()
