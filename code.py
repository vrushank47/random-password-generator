# length of the character
#should contain uppercase
#should contain spl characters
#should contain digits 


# get all available characters
# randomly pick characters up to the length
# ensure atleast one of each character type
# ensure length is valid


import random 
import string 
from tkinter import *

def generate_password():
    length = int (entry_length.get().strip())
    include_uppercase= var_uppercase.get()
    include_splcharacters = var_special.get()
    include_digits = var_digits.get()




    if length < 5:
        print("the password must be atleast 4 characters long")
        return
    

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase  else ""
    digits = string.digits if include_digits else ""
    special = string.punctuation if include_splcharacters else ""
    all_characters = lower + upper + digits +special



    required_characters= []
    if include_uppercase:
        required_characters.append(random.choice(upper))
    if include_splcharacters:
        required_characters.append(random.choice(special))
    if include_digits:
        required_characters.append(random.choice(digits))
    
    

    required_length = length - len(required_characters)
    password = required_characters 

    for _ in range (required_length):
        characters = random.choice(all_characters)
        password.append(characters)

    random.shuffle(password)

    str_password = "".join(password)
    result_label.config(text="generate password :" + str_password)
    return
root = Tk()
root.title("passwrod generator")

# length input
Label(root , text="password length :").pack()
entry_length = Entry(root)
entry_length.pack()


# options
var_uppercase = BooleanVar()
Checkbutton(root , text="include uppercase", variable=var_uppercase).pack()

var_digits = BooleanVar()
Checkbutton(root , text= "enter digits" , variable=var_digits).pack()

var_special = BooleanVar()
Checkbutton(root , text="include special characters" , variable=var_special).pack()


#generate button
button = Button(root , text="generate password", command=generate_password).pack()

# result
result_label = Label(root , text="")
result_label.pack()



root.mainloop()
