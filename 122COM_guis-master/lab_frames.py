import sys
from tkinter import *

class Gui:
	number = ""
	operand1 = 0
	operand2 = 0
	result = 0
	clr = False
	def __init__(self, root):
		self.root = root
		
		self.label = Label(self.root,text=0)
		self.label.pack(fill=BOTH,expand=True)

		self.frame = Frame(self.root)
		self.frame.pack(fill=BOTH,expand=False)

		self.button1 = Button(self.frame, text='1', command = lambda a=1: self.button_press(a))
		self.button2 = Button(self.frame, text='2', command = lambda a=2: self.button_press(a))
		self.button3 = Button(self.frame, text='3', command = lambda a=3: self.button_press(a))
		self.button1.pack(side=LEFT,fill=BOTH,expand=True)
		self.button2.pack(side=LEFT,fill=BOTH,expand=True)
		self.button3.pack(side=LEFT,fill=BOTH,expand=True)
		
		self.frame2 = Frame(self.root)
		self.frame2.pack(fill=BOTH,expand=False)
		
		self.button4 = Button(self.frame2, text='4', command = lambda a=4: self.button_press(a))
		self.button5 = Button(self.frame2, text='5', command = lambda a=5: self.button_press(a))
		self.button6 = Button(self.frame2, text='6', command = lambda a=6: self.button_press(a))
		self.button4.pack(side=LEFT,fill=BOTH,expand=True)
		self.button5.pack(side=LEFT,fill=BOTH,expand=True)
		self.button6.pack(side=LEFT,fill=BOTH,expand=True)
		
		self.frame3 = Frame(self.root)
		self.frame3.pack(fill=BOTH,expand=False)
		
		self.button7 = Button(self.frame3, text='7', command = lambda a=7: self.button_press(a))
		self.button8 = Button(self.frame3, text='8', command = lambda a=8: self.button_press(a))
		self.button9 = Button(self.frame3, text='9', command = lambda a=9: self.button_press(a))
		self.button7.pack(side=LEFT,fill=BOTH,expand=True)
		self.button8.pack(side=LEFT,fill=BOTH,expand=True)
		self.button9.pack(side=LEFT,fill=BOTH,expand=True)
		
		self.frame4 = Frame(self.root)
		self.frame4.pack(fill=BOTH,expand=False)
		
		self.button0 = Button(self.frame4, text='0', command = lambda a=0: self.button_press(a))
		self.buttonPlus = Button(self.frame4, text='+', command = lambda: self.btn_plus())
		self.buttonEquals = Button(self.frame4, text='=', command = lambda: self.calculate())
		self.button0.pack(side=LEFT,fill=BOTH,expand=True)
		self.buttonPlus.pack(side=LEFT,fill=BOTH,expand=True)
		self.buttonEquals.pack(side=LEFT,fill=BOTH,expand=True)
		self.frame5 = Frame(self.root)
		self.frame5.pack(fill=BOTH,expand=False)
		self.buttonclr = Button(self.frame5, text='clr', command = lambda: self.Btn_Clr())
		self.buttonclr.pack(side=LEFT,fill=BOTH,expand=True)
	def button_press(self, val):
		if Gui.clr == False:
			Gui.number += str(val)
		else:
			Gui.number = str(val)
			Gui.clr = False
		self.label.config(text=Gui.number)
	def btn_plus(self):
		self.calculate()
		Gui.operand1 = self.label.cget("text")
		if Gui.operand2 ==  0:
			Gui.operand2 = int(Gui.operand1) + 0
		else:
			Gui.operand2 = int(Gui.operand1) + int(Gui.operand2)
		self.label.config(text = "")
		Gui.clr = True
	def calculate(self):
		Gui.operand2 = int(Gui.number)
		Gui.operand1 = int(Gui.operand1)
		Gui.result = int(Gui.operand1) + int(Gui.operand2)
		self.label.config(text=Gui.result)
		Gui.clr = True

	def Btn_Clr(self):
		Gui.operand1 = 0
		Gui.operand2 = 0
		Gui.number = ""
		self.label.config(text = 0)
		
def main():
	root = Tk()
	# set the starting size of the window
	#root.geometry('%dx%d' % (320,240))
	gui = Gui(root)
	root.mainloop()


if __name__ == '__main__':
	sys.exit(main())
