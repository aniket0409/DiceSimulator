import random
from tkinter import *


def a2d(a):
    faces = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    s = ''
    for i in a:
        s += faces[i - 1]
    return s


def a2s(a):
    s = ''
    for i in a:
        s += str(i) + " "
    return s[:-1]


def submit():
    def roll():
        global n
        # s = n.get()
        num = int(n.get())
        if num > 4 or num<1:

            newwind.destroy()
            l1.config(text="Invalid number of dices please enter valid number")
            return
        else:
            l1.config(text="Press \"Submit\" to continue or \"Quit\" to end")
        op = []
        for i in range(num):
            op.append(random.randint(1, 6))
        l2.config(text=f'{a2d(op)}')
        # l1.config(text=f'{num}')
        l2.pack()

    newwind = Toplevel(root1)
    newwind.title = "Dice Simulator"
    newwind.geometry("700x450")
    l2 = Label(newwind, text='', font=("times", 150))
    b1 = Button(newwind, text="Roll the dice", command=roll)
    b1.place(x=310, y=400)
    b2 = Button(newwind, text="Quit", command=newwind.destroy)
    b2.place(x=390, y=400)


root1 = Tk()
root1.geometry("450x100")
root1.title("Dice Simulator")
l1 = Label(root1, text='', font=("times", 10))
l1.config(text='Enter the number of dice(s)')
l1.pack()
n = Entry(root1, width=60)
n.focus_set()
n.pack()
sub = Button(root1, text="Submit", command=submit)
sub.place(x=290, y=50)
q = Button(root1, text="Quit", command=root1.destroy)
q.place(x=350, y=50)
root1.mainloop()
