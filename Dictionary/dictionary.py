import json
from difflib import get_close_matches
from tkinter import *

data = json.load(open("meanings.json","r"))

window = Tk()
window.geometry("800x275")
window.title("DICTIONARY")

class dict :
	def translate(self) :
		try:
			self.b10.grid_remove()
		except:
			pass	
		if e1.get() != "" :
			file = open("history.txt",'a+')
			file.seek(0)
			if e1.get() not in file :
				file.write(e1.get()+'\n')
			else:
				pass	
			file.close()
			if e1.get().lower() in data :
				try:	
					self.t2.grid_remove()
					self.b2.grid_remove()
					self.b3.grid_remove()
					t1.delete(0,END)
					output = data[e1.get().lower()]
					for item in output:
						t1.insert(END,item+'\n')
				except:
					t1.delete(0,END)
					output = data[e1.get().lower()]
					for item in output:
						t1.insert(END,item+'\n')						
						
			elif e1.get().title() in data :
				try:	
					self.t2.grid_remove()
					self.b2.grid_remove()
					self.b3.grid_remove()			
					t1.delete(0,END)
					output = data[e1.get().title()]
					for item in output:
						t1.insert(END,item+'\n')
				except:
					t1.delete(0,END)
					output = data[e1.get().title()]
					for item in output:
						t1.insert(END,item+'\n')				

			elif e1.get().upper() in data :
				try:	
					self.t2.grid_remove()
					self.b2.grid_remove()
					self.b3.grid_remove()			
					t1.delete(0,END)
					output = data[e1.get().upper()]
					for item in output:
						t1.insert(END,item+'\n')
				except:
					t1.delete(0,END)
					output = data[e1.get().upper()]
					for item in output:
						t1.insert(END,item+'\n')				
							
			elif e1.get() not in data:
				try:
					try:	
						self.t2.grid_remove()
						self.b2.grid_remove()
						self.b3.grid_remove()
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
						pass
		else:
			t1.delete(0,END)
			t1.insert(END,"NO WORD TYPED!!!!")				
	
	def translate2(self):
		try:
			self.b10.grid_remove()
		except:
			pass		
		t1.delete(0,END)
		output = data[self.matches]
		for item in output:
			t1.insert(END,item+'\n')
		e1.delete(0,END)
		e1.insert(0,self.matches)
		file = open("history.txt",'a+')
		file.seek(0)
		file.write(e1.get()+'\n')
		file.close()	
		self.t2.grid_remove()
		self.b2.grid_remove()
		self.b3.grid_remove()

	def translate3(self):
		try:
			self.b10.grid_remove()
		except:
			pass		
		t1.delete(0,END)
		output = "THANK YOU!!!!!"	
		t1.insert(END,output)
		self.t2.grid_remove()
		self.b2.grid_remove()
		self.b3.grid_remove()

	def history(self):
		self.b10 = Button(window,text="SEARCH SELECTED",command=lambda:[d.print_me(),d.translate()])
		self.b10.grid(row=0,column=3)
		try :
			e1.delete(0,END)
			t1.delete(0,END)
			file = open("history.txt",'r')
			for index,self.line in enumerate(file):
				self.line = self.line.rstrip()
				r = str(index+1)+'. '+self.line
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
			for index,self.line in enumerate(file):
				self.line = self.line.rstrip()
				r = str(index+1)+'. '+self.line
				t1.insert(END,r)
			file.seek(0)
			file.close()

	def clear_history(self):
		try:
			self.b10.grid_remove()
		except:
			pass		
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

	def print_me(self):
		clicked_items = t1.curselection()
		for self.line in clicked_items:
			a = t1.get(self.line)
			try:
				if type(int(a[:7]))==int:
					e1.delete(0,END)
					e1.insert(END,a[9:])
			except:
				try :
					if type(int(a[:6]))== int:
						e1.delete(0,END)
						e1.insert(END,a[8:])
				except:
					try:
						if type(int(a[:5]))==int:
							e1.delete(0,END)
							e1.insert(END,a[7:])	
					except:
						try :
							if type(int(a[:4]))==int:
								e1.delete(0,END)
								e1.insert(END,a[6:])
						except:
							try:
								if type(int(a[:3]))==int:
									e1.delete(0,END)
									e1.insert(END,a[5:])	
							except:
								try :
									if type(int(a[:2]))==int:
										e1.delete(0,END)
										e1.insert(END,a[4:])
								except:
									try:
										if type(int(a[:1])) == int:
											e1.delete(0,END)
											e1.insert(END,a[3:])
									except:
										try:
											if type(int(a[:0]))==int:
												e1.delete(0,END)
												e1.insert(END,a[2:])
										except:
											t1.delete(0,END)
											t1.insert(END,"ERROR")							

d = dict()

l1 = Label(window,text="Enter the word")
l1.grid(row = 0 , column = 0)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row = 0,column = 1)

b1 = Button(window,text = "Execute",command=d.translate)
b1.grid(row = 0,column=2)

t1 = Listbox(window,height=10,width=100,selectmode=SINGLE)
t1.grid(row=4,column=0,columnspan=3)

sb1 = Scrollbar(window,orient=VERTICAL,command=t1.yview)
sb1.grid(row = 2,column=3,rowspan=3)

sb2 = Scrollbar(window,orient=HORIZONTAL,command=t1.xview)
sb2.grid(row = 5,column=0,columnspan=5)

b4 = Button(window,text="History",command=d.history)
b4.grid(row=3,column=6)

b5 = Button(window,text="Quit",command=d.close_window)
b5.grid(row=6,column=6)

b6 = Button(window,text="Clear History",command=d.clear_history)
b6.grid(row=4,column=6)

window.bind('<Return>', lambda event=None: b1.invoke())
window.bind('<Control-h>', lambda event=None: b4.invoke())
window.bind('<Control-q>', lambda event=None: b5.invoke())

window.mainloop()
