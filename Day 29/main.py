
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
CHARS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
'!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  if len(p_entry.get()) > 0:
    p_entry.delete(0, END)
  new_password = ""
  for _ in range(15):
    r_char = random.choice(CHARS)
    new_password += r_char
  p_entry.insert(0, new_password)
  pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
  website = w_entry.get()
  user = e_entry.get()
  password = p_entry.get()
  x = len(user)
  y = len(password)
  new_data = {
    website: {
      "user": user,
        "password": password,
    }
  }
    
  if not user or not password:
        messagebox.showinfo(title="Error", message="You must include both a username/email and a password")
        return

  file_path = r"Day 29\paswords.json"  # Use raw string for file path

  try:
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            # Load existing data
            data = json.load(file)
    else:
        data = {}
            
    # Update data with new entry
    data.update(new_data)
        
    with open(file_path, "w") as file:
        # Save updated data
        json.dump(data, file, indent=4)
        
    w_entry.delete(0, END)
    p_entry.delete(0, END)

  except Exception as e:
    messagebox.showinfo(title="Error", message=f"An error occurred: {e}")

# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Password Manager")
screen.configure(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_logo =  PhotoImage(file="Day 29\logo.png")

canvas.create_image(100, 100, image=lock_logo)
canvas.grid(row=0, column=1)

#-----Website text
w_text = Label(screen, text="Website:")
w_text.grid(row=1, column=0)

#-----Email/Password Text
e_text = Label(screen, text="Email/username:")
e_text.grid(row=2, column=0)

#----- Password Text
p_text = Label(screen, text="Password:", padx=10)
p_text.grid(row=3, column=0)

#---- Website textbox
w_entry = Entry(width=35)
w_entry.grid(column=1, row=1, columnspan=2)
w_entry.focus()

#---- Email/Username textbox
e_entry = Entry(width=35)
e_entry.grid(column=1, row=2, columnspan=2)
e_entry.insert(0, "Example@email.com")

#---- Password textbox
p_entry = Entry(width=30)
p_entry.grid(column=1, row=3,)

#----- Generate Password Button
password_button = Button(height=1, width=15, text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

#-----Add button
add_button = Button(height=1, width=35, text="add", command=add)
add_button.grid(column=1, row=4, columnspan=2)


#Leave at bottom
screen.mainloop()
