import tkinter as tk
import passgenfun as fun
import data
from display import hold
from checkP import check
from printfile import data_out
from securedfamilydb import fam_db_chk

def generate_password():
    def generate():
        ptype = password_type.get().lower()
        if ptype == 'weak':
            password = fun.generate.weakP()
        elif ptype == 'medium':
            password = fun.generate.medP()
        elif ptype == 'strong':
            upto = int(upto_entry.get())
            password = fun.generate.strongP(upto)
        else:
            return

        output_label.config(text=f"Generated Password: {password}")
        save_password(password)

    def save_password(password):
        response = tk.messagebox.askquestion("Save Password", "Would you like to save this password?")
        if response == 'yes':
            data_out(password)

    generate_window = tk.Toplevel(root)
    generate_window.title("Generate Password")

    password_type = tk.StringVar()
    tk.Label(generate_window, text="Choose Password Type:").pack()
    tk.Radiobutton(generate_window, text="Weak", variable=password_type, value="weak").pack()
    tk.Radiobutton(generate_window, text="Medium", variable=password_type, value="medium").pack()
    tk.Radiobutton(generate_window, text="Strong", variable=password_type, value="strong").pack()

    upto_label = tk.Label(generate_window, text="Enter Password Length (8~64):")
    upto_label.pack()
    upto_entry = tk.Entry(generate_window)
    upto_entry.pack()

    generate_button = tk.Button(generate_window, text="Generate", command=generate)
    generate_button.pack()

    output_label = tk.Label(generate_window, text="")
    output_label.pack()

root = tk.Tk()
root.title("Password Generator")

commands = [
    "Generate only a random Password",
    "Generate - Manage and save a Password",
    "Show Saved Accounts and Passwords",
    "Check how strong your Password is!",
    "STOP"
]

for idx, command in enumerate(commands):
    tk.Label(root, text=f"{idx}. {command}").pack()

command_entry = tk.Entry(root)
command_entry.pack()

def handle_command():
    command = command_entry.get()
    if command == "0":
        root.destroy()
    elif command == "1":
        generate_password()
    elif command == "2":
        data.menu()
    elif command == "3":
        fam_db_chk()
        data.show_saved()
    elif command == "4":
        Password = tk.simpledialog.askstring("Password Check", "Enter your Password to be checked:")
        run = check.PasswordCheck(Password)
    else:
        print("No choice selected")

tk.Button(root, text="Enter Command", command=handle_command).pack()

root.mainloop()
