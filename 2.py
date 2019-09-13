from tkinter import *

def printhello():
    print("hello")

class Window:
    def __init__(self, root, title, label):
        root.wm_minsize(500,500)
        root.title(title)
        lbl1 = Label(root, text=label)
        lbl1.pack()
        btn1 = Button(root, text = "Help", command = printhello)
        btn1.pack()
        quitbtn = Button(root, text = "Quit", command = root.quit)
        quitbtn.pack()
        root.mainloop()




root = Tk()
myWin = Window(root, 'Window 1', 'Yes!')
myWin2 = Window(root, 'Window 2', 'No...')
