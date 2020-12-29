import json
from difflib import get_close_matches
from tkinter import *
from datetime import datetime

data = json.load(open("meanings.json","r"))

window = Tk()
window.geometry("730x250")
window.title("DICTIONARY")

class dict :
	def translate(self) :
		file = open("history.txt",'a+')
		file.seek(0)
		file.write(e1.get()+'                   '+str(datetime.now())+'\n')
		file.close()
		if e1.get().lower() in data :
			t1.delete(0,END)
			output = data[e1.get().lower()]
			for item in output:
				t1.insert(END,item+'\n')
					
		elif e1.get().title() in data :
			t1.delete(0,END)
			output = data[e1.get().title()]
			for item in output:
				t1.insert(END,item+'\n')
					
		elif e1.get().upper() in data :
			t1.delete(0,END)
			output = data[e1.get().upper()]
			for item in output:
				t1.insert(END,item+'\n')
			
		elif e1.get() not in data:
			try:
				t1.delete(0,END)
				self.matches = get_close_matches(e1.get(),data.keys(),cutoff=0.75)[0]
				a  = 'Do you mean by'+' '+self.matches+' '+"instead??"
				self.t2 = Listbox(window,height=1,width=40)
				self.t2.grid(row=1,column=0,columnspan=2)
				self.t2.delete(0,END)
				self.t2.insert(END,a)
			
				self.b2 = Button(window,text="YES",command=d.translate2)
				self.b2.grid(row=2,column=0)
				
				self.b3 = Button(window,text="NO",command=d.translate3)
				self.b3.grid(row=2,column=1)
			except :
				t1.delete(0,END)
				t1.insert(END,"Can't understand the word you typed")
				try:	
					self.t2.grid_remove()
					self.b2.grid_remove()
					self.b3.grid_remove()
				except:
					t1.delete(0,END)
					t1.insert(END)
	
	def translate2(self):
		t1.delete(0,END)
		output = data[self.matches]
		for item in output:
			t1.insert(END,item+'\n')
		e1.delete(0,END)
		e1.insert(0,self.matches)
		file = open("history.txt",'a+')
		file.seek(0)
		file.write(e1.get()+'                   '+str(datetime.now())+'\n')
		file.close()	
		self.t2.grid_remove()
		self.b2.grid_remove()
		self.b3.grid_remove()

	def translate3(self):
		t1.delete(0,END)
		output = "THANK YOU!!!!!"	
		t1.insert(END,output)
		self.t2.grid_remove()
		self.b2.grid_remove()
		self.b3.grid_remove()

	def history(self):
		try :
			e1.delete(0,END)
			t1.delete(0,END)
			file = open("history.txt",'r')
			for index,line in enumerate(file):
				line = line.rstrip()
				r = str(index+1)+'. '+line
				t1.insert(END,r)
			file.seek(0)
			file.close()
			self.t2.grid_remove()
			self.b2.grid_remove()
			self.b3.grid_remove()
		except:
			e1.delete(0,END)
			t1.delete(0,END)
			file = open("history.txt",'r')
			for index,line in enumerate(file):
				line = line.rstrip()
				r = str(index+1)+'. '+line
				t1.insert(END,r)
			file.seek(0)
			file.close()

	def clear_history(self):
		try :
			e1.delete(0,END)
			t1.delete(0,END)
			open("history.txt",'w').close()
			file = open("history.txt",'r')
			for line in file:
				line = line.rstrip()
				t1.insert(END,line)
			file.seek(0)
			file.close()
			self.t2.grid_remove()
			self.b2.grid_remove()
			self.b3.grid_remove()
		except:
			e1.delete(0,END)
			t1.delete(0,END)
			open("history.txt",'w').close()
			file = open("history.txt",'r')
			for line in file:
				line = line.rstrip()
				t1.insert(END,line)
			file.seek(0)
			file.close()

	def close_window(self):
		window.destroy()

d = dict()

l1 = Label(window,text="Enter the word")
l1.grid(row = 0 , column = 0)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row = 0,column = 1)

b1 = Button(window,text = "Execute",command=d.translate)
b1.grid(row = 0,column=2)

t1 = Listbox(window,height=10,width=100)
t1.grid(row=4,column=0,columnspan=3)

sb1 = Scrollbar(window,orient=VERTICAL,command=t1.yview)
sb1.grid(row = 2,column=3,rowspan=3)

sb2 = Scrollbar(window,orient=HORIZONTAL,command=t1.xview)
sb2.grid(row = 5,column=0,columnspan=5)

b4 = Button(window,text="History",command=d.history)
b4.grid(row=0,column=6)

b5 = Button(window,text="Quit",command=d.close_window)
b5.grid(row=5,column=6)

b6 = Button(window,text="Clear History",command=d.clear_history)
b6.grid(row=4,column=6)

window.bind('<Return>', lambda event=None: b1.invoke())
window.bind('<Control-h>', lambda event=None: b4.invoke())
window.bind('<Control-q>', lambda event=None: b5.invoke())

window.mainloop()
