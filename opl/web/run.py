import os
import http.server
import threading
import json
from pathlib import Path
import shutil
import sys
import tkinter as tk
from tkinter import filedialog

mycwd = os.getcwd()



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

def server_start(port):
    os.chdir(mycwd)
    Path("ports/" + str(port)).mkdir(parents=True, exist_ok=True)
    os.chdir(mycwd)
    os.chdir('ports/' + str(port))
    exec("""
class StoppableHTTPServer(http.server.HTTPServer):
    os.chdir(mycwd)
    os.chdir('ports/' + '""" + str(port) + """')
    def run(self):
        os.chdir(mycwd)
        os.chdir('ports/' + '""" + str(port) + """')
        try:
            os.chdir(mycwd)
            os.chdir('ports/' + '""" + str(port) + """')
            self.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            # Clean-up server (close socket, etc.)
            self.server_close()
    """, globals())
    exec('global s' + str(port))
    exec("""s""" + str(port) + """ = StoppableHTTPServer(("127.0.0.1",""" + str(port) + """),
                             http.server.SimpleHTTPRequestHandler)""", globals())

    # Start processing requests
    exec('global t' + str(port))
    exec('t' +  str(port) + ' = threading.Thread(None, ' + 's' + str(port) + '.run)', globals())
    exec('t' + str(port) + '.start()', globals())
    print("started server: hosting on localhost:" + str(port))


def server_quit(port):
    os.chdir(mycwd)
    os.chdir('ports')
    shutil.rmtree(str(port))
    exec('s' + str(port) + '.shutdown()', globals())
    exec('t' + str(port) + '.join()', globals())
    os.chdir(mycwd)


def loadfile(port):
    os.chdir(mycwd)
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    file_folder = file_path.split("/")
    file_folder.pop()
    os.chdir('/'.join(file_folder))
    with add_path('/'.join(file_folder)):
        g = open(file_path, "r")
        h = g.read()
    os.chdir(mycwd)
    os.chdir("ports/" + str(port))
    with add_path('ports/' + str(port)):
        f = open(file_path.split("/")[-1], "w")
        print(file_path.split("/")[-1])
        f.write(h)
        f.close()