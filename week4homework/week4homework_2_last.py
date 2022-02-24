import random
import string
import tkinter as tk

def generate_random_password():

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation


    select_lower = random.sample(lower,4)
    select_upper = random.sample(upper,2)
    select_numbers= random.sample(numbers,2)
    select_symbols= random.sample(symbols,2)

    a = select_upper + select_lower + select_numbers + select_symbols
    random.shuffle(a)

    password = ''.join(a)
    print(password)

    label.config(text=password)


window = tk.Tk()

window.title("Random Password Generator")
window.geometry("600x300")


key_application = tk.Frame(window)
key_application.grid()


# label
label_txt = tk.Label(key_application, text="Password:", font="arial 15 bold")
label_txt.grid(padx=110, pady=10)


# label
label = tk.Label(key_application, text="Please push the botton to generate the new password ", font="arial 12")
label.grid(padx=110, pady=20)


# button
button1 = tk.Button(key_application, text=" GENERATE ", width=50, height=5, command=generate_random_password)
button1.grid(padx=110, pady=40)

window.mainloop()