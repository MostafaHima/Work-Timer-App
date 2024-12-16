import random
from tkinter import *


def color():
    colors = [random.randint(0,255) for _ in range(3)]
    return tuple(colors)


def clicked():
    new_text = input.get()
    label.config(text=new_text)
    print(input.get())

# Setup Screen
window = Tk()
window.title("My First GUI Program.")
window.minsize(width=600, height=400)

# Text in Head
label = Label(text="Halo", font=("italic", 20, "italic"), foreground="red")
label.pack(side="top")

# Enter button
button = Button(text="click Me", activebackground="purple", font=('Arial', 10, "bold"), command=clicked)
button.pack(side="top")


# Enter Box
input = Entry(width=50, )
input.pack()
input.insert(END, "Fuck YOu")

# Text Box
text = Text(width=50, height=5, background="white", foreground="red")
text.insert(END, "Hello Desha ")
print(text.get("0.10", END))
text.focus()
text.pack()


# spain Box
def spain_box():
    print(spain_box.get())


spain_box = Spinbox(from_=1, to=100, width=10, command=spain_box)
spain_box.pack()


# Scale
def scale(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale, background="green")
scale.pack(side="right")

# check button used
def check_button_used():
   print(check_state.get())

check_state = IntVar()
check_button = Checkbutton(text="On", variable=check_state, command=check_button_used)
check_button.pack()


# Choice one variable
def check_used():
    print(radio_state.get())

radio_state = IntVar()
radio_button_one = Radiobutton(text="option1", variable=radio_state, command=check_used, value=1)
radio_button_two = Radiobutton(text="option2",variable=radio_state, command=check_used, value=2)
radio_button_one.pack()
radio_button_two.pack()


# list box
def list_box_used(event):
    print(list_box.get(list_box.curselection()))

list_box = Listbox(height=5)
fruits = ["An Apple", "An orange", "A Pear", 'A banana']
for item in fruits:
    list_box.insert(fruits.index(item), item)
list_box.bind("<<ListboxSelect>>", list_box_used)
list_box.pack()





window.mainloop()

