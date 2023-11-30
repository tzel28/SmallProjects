"""We're going to build GUI calculator using Tkinter from Python"""
"Developer Thomas Zelaya"

# Import functions needed for this application

import tkinter as tk

field_text = ""  # This will be the field where the numbers are displayed in


def add_to_field(sth):
    """This is the function used to add to the field """
    global field_text  # add this manipulates variables because it will concatenate to the fill_text
    field_text = field_text + str(sth)  # sth stand for something b/c we want the field to be filled with something
    field.delete("1.0", "end")  # this will delete the previous content
    field.insert("1.0", field_text)  # will add text in the first field


def calculate():
    """Function will calculate whatever is in the field text and show the result"""
    global field_text
    result = str(eval(field_text))  # This will calculate the result and then convert it into a string
    # update the field with the result variable
    field.delete("1.0", "end")  # this will delete the previous content
    field.insert("1.0", result)  # will replace the first content with the result


def clear():
    """clear button will rest the field text & delete the contents of the field"""
    global field_text
    field_text = ""  # rest the field text
    field.delete("1.0", "end")  # this will delete the previous content


window = tk.Tk()
window.geometry("300x300")  # making a window in our cal
field = tk.Text(window, height=2, width=21, font=("Times New Roman", 20))  # adding the rest of the styles to the cal
field.grid(row=1, column=1, columnspan=4)  # will occupy four columns


"""We will now add the buttons to be displayed on the calculator """
btn_1 = tk.Button(window, text="1", command=lambda: add_to_field(1), width=5, font=("Times New Roman", 14))
btn_1.grid(row=4, column=1)

btn_2 = tk.Button(window, text="2", command=lambda: add_to_field(2), width=5, font=("Times New Roman", 14))
btn_2.grid(row=4, column=2)

btn_3 = tk.Button(window, text="3", command=lambda: add_to_field(3), width=5, font=("Times New Roman", 14))
btn_3.grid(row=4, column=3)

btn_4 = tk.Button(window, text="4", command=lambda: add_to_field(4), width=5, font=("Times New Roman", 14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(window, text="5", command=lambda: add_to_field(5), width=5, font=("Times New Roman", 14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(window, text="6", command=lambda: add_to_field(6), width=5, font=("Times New Roman", 14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(window, text="7", command=lambda: add_to_field(7), width=5, font=("Times New Roman", 14))
btn_7.grid(row=2, column=1)

btn_8 = tk.Button(window, text="8", command=lambda: add_to_field(8), width=5, font=("Times New Roman", 14))
btn_8.grid(row=2, column=2)

btn_9 = tk.Button(window, text="9", command=lambda: add_to_field(9), width=5, font=("Times New Roman", 14))
btn_9.grid(row=2, column=3)

btn_0 = tk.Button(window, text="0", command=lambda: add_to_field(8), width=5, font=("Times New Roman", 14))
btn_0.grid(row=5, column=1)

""" Operations Button """

btn_plus = tk.Button(window, text="+", command=lambda: add_to_field("+"), width=5, font=("Times New Roman", 14))
btn_plus.grid(row=4, column=4)

btn_minus = tk.Button(window, text="-", command=lambda: add_to_field("-"), width=5, font=("Times New Roman", 14))
btn_minus.grid(row=5, column=4)

btn_times = tk.Button(window, text="*", command=lambda: add_to_field("*"), width=5, font=("Times New Roman", 14))
btn_times.grid(row=3, column=4)

btn_division = tk.Button(window, text="/", command=lambda: add_to_field("/"), width=5, font=("Times New Roman", 14))
btn_division.grid(row=2, column=4)

btn_clear = tk.Button(window, text="clear", command=lambda: clear(), width=5, font=("Times New Roman", 14))
btn_clear.grid(row=5, column=3)

btn_decimal = tk.Button(window, text=".", command=lambda: add_to_field("."), width=5, font=("Times New Roman", 14))
btn_decimal.grid(row=5, column=2)

btn_open_parenthesis = tk.Button(window, text="(", command=lambda: add_to_field("("), width=5,
                                 font=("Times New Roman", 14))
btn_open_parenthesis.grid(row=6, column=1)

btn_close_parenthesis = tk.Button(window, text=")", command=lambda: add_to_field(")"), width=5,
                                  font=("Times New Roman", 14))
btn_close_parenthesis.grid(row=6, column=2)

btn_equal = tk.Button(window, text="=", command=lambda: calculate(), width=5, font=("Times New Roman", 14))
btn_equal.grid(row=6, column=3, columnspan=3)

window.mainloop()
