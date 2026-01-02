# def add(*ns):
#     t = 0
#     for n in ns:
#         t += n
#     return t

# print(add(1, 2, 3))       # 6
# print(add(1, 2, 3, 4, 5)) # 15

# class Calc:
#     def __init__(self, **kvs):
#         self.n = kvs.get('n')
#         self.a = kvs.get('a')

# my_calc = Calc(n=5, a=10)
# print(my_calc.n)


from tkinter import *

window = Tk()
window.title("My First GUI!")
window.minsize(width=500, height=300)

n = 0
def button_clicked():
    global n 
    n += 1
    my_label.config(text=f"{n} clicks!")
    print("I got clicked")

my_label = Label(text="0 clicks!", font=("Arial", 24, "bold", "italic"))
my_label.pack()

button = Button(text="Click Me!", command=button_clicked)
button.pack()




window.mainloop()