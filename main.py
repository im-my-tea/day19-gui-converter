from tkinter import *

window = Tk()
window.title("Miles to KMs Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20, bg='aqua')


def mls_to_kms():
    mls = float(miles_input.get())
    km = mls * 1.609
    km_result_label.config(text=f"{km}")

miles_input = Entry(width=7)
miles_label = Label(text="Miles")
is_equal_to_label = Label(text="is equal to")
km_result_label = Label(text="0")
kms_label = Label(text="Km")
calc_button = Button(text="Calculate", command=mls_to_kms)

miles_input.grid(row=0, column=1)
miles_label.grid(row=0, column=2)
is_equal_to_label.grid(row=1, column=0)
km_result_label.grid(row=1, column=1)
kms_label.grid(row=1, column=2)
calc_button.grid(row=2, column=1)



window.mainloop()