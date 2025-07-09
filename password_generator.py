import tkinter as tk
from tkinter import messagebox
from random import choice
from string import ascii_letters, digits, punctuation

def create_password(length):
    if length < 4:
        return None
    characters = ascii_letters + digits + punctuation
    return ''.join(choice(characters) for _ in range(length))

def handle_generate():
    try:
        length_val = int(length_input.get())
        password = create_password(length_val)
        if password:
            result_display.config(text=f"Generated Password:\n{password}")
        else:
            messagebox.showwarning("Too Short", "Please enter at least 4 characters.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Only whole numbers are allowed.")

def clear_fields():
    length_input.delete(0, tk.END)
    result_display.config(text="")


window = tk.Tk()
window.title("CodSoft Internship Task 1")
window.geometry("420x270")
window.configure(bg="white")

heading = tk.Label(window, text="CodSoft Password Generator", font=("Verdana", 15, "bold"), bg="white", fg="black")
heading.pack(pady=12)


prompt = tk.Label(window, text="Choose password length:", font=("Verdana", 11), bg="white")
prompt.pack()

length_input = tk.Entry(window, font=("Verdana", 12), justify="center", width=10)
length_input.pack(pady=6)


btn_frame = tk.Frame(window, bg="white")
btn_frame.pack()

generate_btn = tk.Button(btn_frame, text="Generate", command=handle_generate, font=("Verdana", 11),
bg="green", fg="white", width=12)
generate_btn.grid(row=0, column=0, padx=8)

clear_btn = tk.Button(btn_frame, text="Clear", command=clear_fields, font=("Verdana", 11),
 bg="red", fg="white", width=8)
clear_btn.grid(row=0, column=1)


result_display = tk.Label(window, text="", font=("Verdana", 11), bg="white", fg="black")
result_display.pack(pady=15)

window.mainloop()