import json
import string
from random import choice, shuffle
import pyperclip
from tkinter import *
from tkinter import messagebox

def generate_pass():
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = list(string.punctuation)

    password_list = (
        [choice(letters) for _ in range(4, 8)] +
        [choice(numbers) for _ in range(2, 6)] +
        [choice(symbols) for _ in range(2, 6)]
    )
    shuffle(password_list)
    password_gen = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password_gen)
    pyperclip.copy(password_gen)


def find_password():
    website = website_entry.get().strip().lower()
    if not website:
        messagebox.showinfo(title="INFO", message="Please enter a website to search for.")
        return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showinfo(title="INFO", message="No Data found.")
        return

    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
    else:
        messagebox.showinfo(title="INFO", message=f"No Data found for website: {website}")


def save():
    website_raw = website_entry.get()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if not website_raw.strip() or not email or not password:
        messagebox.showinfo(title="OOPS!", message="Empty fields not allowed")
        return

    website = website_raw.strip().lower()  # normalize key
    new_data = {website: {"email": email, "password": password}}

    # load existing data
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if not isinstance(data, dict):
                data = {}
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    # Ask before overwriting existing website entry
    if website in data:
        should_update = messagebox.askyesno(
            title="Confirm overwrite",
            message=f"An entry for '{website}' already exists. Overwrite?"
        )
        if not should_update:
            return

    # update and save the merged data
    data.update(new_data)
    try:
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
    except Exception as e:
        messagebox.showerror(title="Error", message=f"Failed to save data: {e}")
        return

    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ----- UI -----
window = Tk()
window.title("PASSWORD GENERATOR")
window.config(bg="black", padx=50, pady=50)

canvas = Canvas(width=500, height=400, bg="black", highlightthickness=0)
# If pass_gen_logo.png isn't centered correctly, adjust coordinates.
try:
    pass_logo = PhotoImage(file="pass_gen_logo.png")
    canvas.create_image(250, 80, image=pass_logo)
except Exception:
    # If image not found, ignore silently (or you can print a warning)
    pass
canvas.grid(row=0, column=1, columnspan=2)

Label(text="Website:", fg="white", bg="black", font=("Arial", 20)).grid(row=1, column=0, sticky="w")
Label(text="Email:", fg="white", bg="black", font=("Arial", 20)).grid(row=2, column=0, sticky="w")
Label(text="Password:", fg="white", bg="black", font=("Arial", 20)).grid(row=3, column=0, sticky="w")

website_entry = Entry(width=30, font=("Arial", 15))
website_entry.grid(row=1, column=1, padx=5, pady=5)
website_entry.focus()

email_entry = Entry(width=30, font=("Arial", 15))
email_entry.grid(row=2, column=1, padx=5, pady=5)
email_entry.insert(0, "dess@gmail.com")

password_entry = Entry(width=30, font=("Arial", 15))
password_entry.grid(row=3, column=1, padx=5, pady=5)

generate_pass_button = Button(text="Generate Password", width=20, font=("Arial", 10), command=generate_pass)
generate_pass_button.grid(row=2, column=2, padx=5)

add_button = Button(text="Add password", width=20, font=("Arial", 10), command=save)
add_button.grid(row=3, column=2, padx=5)

search_button = Button(text="Search", width=20, font=("Arial", 10), command=find_password)
search_button.grid(row=1, column=2, padx=5)

window.mainloop()
