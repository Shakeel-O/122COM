import sys
from tkinter import *

class Gui:
	def __init__(self, root):
		self.root = root

		self.frame1 = Frame(self.root,borderwidth=10,relief=GROOVE)
		self.frame1.pack()

		self.frame2 = Frame(self.root)
		self.frame2.pack()

		self.frame3 = Frame(self.root)
		self.frame3.pack()

		Button(self.frame1, text=1).pack(side=LEFT)
		Button(self.frame1, text=2).pack(side=LEFT)
		Button(self.frame1, text=3).pack(side=LEFT)
		Button(self.frame2, text=4).pack(side=LEFT)
		Button(self.frame2, text=5).pack(side=LEFT)
		Button(self.frame2, text=6).pack(side=LEFT)
		Button(self.frame3, text=7).pack(side=LEFT)
		Button(self.frame3, text=8).pack(side=LEFT)
		Button(self.frame3, text=9).pack(side=LEFT)

def main():
	root = Tk()
	gui = Gui(root)
	root.mainloop()

if __name__ == '__main__':
	sys.exit(main())
