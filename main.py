from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo(title="OOPS!!", message="You put empty fields!")
    else:
        is_ok = messagebox.askokcancel(title=website_input.get(), message=f"These are the details entered: \n Email:{email_input.get()}"
                               f"\nPassword: {password_input.get()}\nIs it ok to save?")
        if is_ok:
            f = open("data.txt", "a")
            f.write(f"{website_input.get()} | {email_input.get()} | {password_input.get()}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)
            f.close()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)


password = Label(text="Password:")
password.grid(column=0, row=3)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()


email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "lukasbaron@seznam.cz")

password_input = Entry(width=21)
password_input.grid(column=1, row=3)
website_input.focus()


password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3)

add_button = Button(width=36, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)









window.mainloop()