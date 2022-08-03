from tkinter import *
from tkinter.ttk import *

def gui(**args):
    try:
        def Convert(string):
            list1=[]
            list1[:0]=string
            return list1
        d = dict(locals(), **globals())
        exec("root = Tk()", d, d)
        for text, options in args.items():
            text1 = Convert(text)[0].upper()
            text = Convert(text)
            text.pop(0)
            text1 = ''.join(text1) + ''.join(text)
            text = text1
            exec("root.title('GUI')", d, d)
            try:
                exec(text + "(root, " + str(options) + ").pack()", d, d)
            except:
                try:
                    text1 = Convert(text)[0].lower()
                    text = Convert(text)
                    text.pop(0)
                    text1 = ''.join(text1) + ''.join(text)
                    text = text1
                    exec("root." + text + "(\"" + str(options) + "\")", d, d)
                except Exception as e:
                    print("There was an error: " + str(e))
        exec("root.mainloop()", d, d)
    except Exception as e:
        print("There was an error: " + str(e))