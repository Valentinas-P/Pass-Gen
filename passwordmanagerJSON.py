from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
WHITE = "#FFFFFF"
# ---------------------------- SEARCH GENERATOR ------------------------------- #


def find_password():

    website = web_email_u.get()

    try:
        with open("data.json", "r") as pass_data:
            data = json.load(pass_data)
    except FileNotFoundError:
        messagebox.showerror(title="Error Accused!", message="No data file Found!")
    else:
        if website in data:
            messagebox.showinfo(
                title=f"{website}", message=f"Chosen account: \nPlease don't share this info!"
                                                     f"\n{data[website]['email']}\n{data[website]['password']}")
        elif website not in data:
            messagebox.showwarning(title="Warning accused", message="No details for the website exists")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def make_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    results = password_letters + password_numbers + password_symbols
    shuffle(results)

    password = "".join(results)
    web_pass.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = web_email_u.get()
    email_u = web_input.get()
    password = web_pass.get()

    new_data = {website: {
        "email": email_u,
        "password": password,
    }}

    if len(website) < 1:
        messagebox.showwarning(message="Website Error: \nPlease enter more than one character long!")
    elif len(password) < 1:
        messagebox.showwarning(message="Password Error: \nPlease enter more than one character long!")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
                # Updating old data to new data
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            web_email_u.delete(0, END)
            web_pass.delete(0, END)


# ---------------------------- UI SETUP -------------------------------
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:", bg="white")
web_label.grid(row=1, column=0)

web_label_e = Label(text="Email/Username:", bg="white")
web_label_e.grid(row=2, column=0)
web_label = Label(text="Password:", bg="white")
web_label.grid(row=3, column=0)

web_email_u = Entry(width=21)
web_email_u.focus()
web_email_u.grid(row=1, column=1, sticky="EW")

web_input = Entry(width=35)
web_input.insert(0, "example@gmail.com")
web_input.grid(row=2, column=1, columnspan=2, sticky="EW")

web_pass = Entry(width=21)
web_pass.grid(row=3, column=1, sticky="EW")

generate_pass = Button(text="Generate Password", command=make_pass)
generate_pass.grid(row=3, column=2)

search_acc = Button(text="Search", width=14, command=find_password)
search_acc.grid(row=1, column=2, columnspan=2)
#
add_user = Button(text="Add", width=36, command=save)
add_user.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()
