_D='600x600'
_C=False
_B='error'
_A='\n'
import os
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
from pathlib import Path
import sys,io,tkinter.messagebox,urllib.request
def texteditor():
	F=1.0;E='*.*';D='All Files';C='*.oxy';B='Oxygen Files';A='ew';os.chdir(os.getcwd()+'/oxygen/workspace')
	def open_file():
		filepath=askopenfilename(filetypes=[(B,C),(D,E)])
		if not filepath:return
		txt_edit.delete(F,END)
		with open(filepath,'r')as input_file:text=input_file.read();txt_edit.insert(END,text)
		window.title(f"Nitrogen - {filepath}")
	def save_file():
		filepath=asksaveasfilename(defaultextension='.oxy',filetypes=[(B,C),(D,E)])
		if not filepath:return
		with open(filepath,'w')as output_file:text=txt_edit.get(F,END);output_file.write(text)
		window.title(f"Nitrogen - {filepath}")
	class add_path:
		def __init__(self,path):self.path=path
		def __enter__(self):sys.path.insert(0,self.path)
		def __exit__(self,exc_type,exc_value,traceback):
			try:sys.path.remove(self.path)
			except ValueError:pass
	def run_file():
		input=txt_edit.get('1.0',END);old_stdout=sys.stdout;sys.stdout=buffer=io.StringIO()
		with add_path(sys.path[0]+'/oxygen'):
			from oxygen import Oxygen;oxygen=Oxygen(_A+input+_A);result=oxygen.lexer()
			if result[_B]!=_C:print('Lexer: '+result[_B]);sys.exit()
			oxygen.parse(result['tokens'])
		sys.stdout=old_stdout;whatWasPrinted=buffer.getvalue();tkinter.messagebox.showinfo('Nitrogen - Result',whatWasPrinted);buffer.close()
	window=Tk();window.title('Nitrogen');window.resizable(0,0);window.rowconfigure(0,minsize=800,weight=1);window.columnconfigure(1,minsize=800,weight=1);txt_edit=Text(window);fr_buttons=Frame(window,relief=RAISED);btn_open=Button(fr_buttons,text='Open',command=open_file);btn_save=Button(fr_buttons,text='Save As...',command=save_file);btn_run=Button(fr_buttons,text='Run',command=run_file);btn_open.grid(row=0,column=0,sticky=A,padx=5,pady=5);btn_save.grid(row=1,column=0,sticky=A,padx=5,pady=5);btn_run.grid(row=2,column=0,sticky=A,padx=5);fr_buttons.grid(row=0,column=0,sticky='ns');txt_edit.grid(row=0,column=1,sticky='nsew');window.mainloop()
output=os.system('cd oxygen  >/dev/null 2>&1')
if output==0:texteditor()
else:
	def loadinstall():
		B=True;A='value'
		def startnitrogenfrominstall():root1.destroy();os.execl(sys.executable,sys.executable,*sys.argv)
		root.destroy();root1=Tk();root1.title('Install');root1.geometry(_D);textbar=Label(root1,text='Starting');textbar.pack();progress=Progressbar(root1,orient=HORIZONTAL,length=100,mode='determinate');progress.pack(pady=10);progress[A]=20;textbar.config(text='Downloading Oxygen from GitHub');root1.update_idletasks();os.system('git clone https://github.com/arjunj132/oxygen.git');page=urllib.request.urlopen('https://raw.githubusercontent.com/arjunj132/oxygen/nitrogen/oxygen.py');h=open('oxygen/oxygen.py','w');h.write(page.read().decode('utf-8'));h.close();textbar.config(text='Creating bash files...');progress[A]=40;root1.update_idletasks();g=open('nitrogen.sh','w');g.write('# This file is neccacary for Nitrogen to work');os.system('bash nitrogen.sh');progress[A]=60;textbar.config(text='Testing...');root1.update_idletasks();from oxygen.oxygen import Oxygen;oxygen=Oxygen(_A+'print "Test"'+_A);result=oxygen.lexer()
		if result[_B]!=_C:Label(root1,text='Error: '+result[_B])
		else:print('Tested successfully')
		progress[A]=80;textbar.config(text='Setting up text editor...');root1.update_idletasks();print('Check wiki to learn more: https://github.com/arjunj132/oxygen/wiki');Path('oxygen/workspace').mkdir(parents=B,exist_ok=B);progress[A]=100;textbar.config(text='Done installing Oxygen');Button(root1,text='Start Nitrogen Editor',command=startnitrogenfrominstall).pack();root1.update_idletasks();root1.mainloop()
	root=Tk();root.title('Install - Terms');root.geometry(_D);Label(root,text='Welcome to Nitrogen, the reccomended way to install Oxygen.').pack();Label(root,text='Please read the following information.').pack();message='Introdution:     \nHello! You are installing a fresh new copy of the Oxygen Programming Language. Plese read the text below and agree to install Oxygen.\n\n\nWhat\'s new:\nhttps://github.com/arjunj132/oxygen/releases/\n\n\nHow to use:\nJust use Nitrogen editor to run the Oxygen files. Or use command line:\npython3 -m runfile file.oxy\n\n\n\nLicense:\n\nMIT License\n\nCopyright (c) 2022 arjunj132\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n';f=Frame(root);f.pack();text_box=Text(f,height=20,width=40);text_box.pack(side='left');text_box.insert('end',message);text_box.config(state='disabled');scrollb=Scrollbar(f,command=text_box.yview);scrollb.pack(side=RIGHT,fill=Y);text_box['yscrollcommand']=scrollb.set;Label(root,text='').pack();agree=Button(root,text='Agree',command=loadinstall);agree.pack();root.mainloop()
