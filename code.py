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

def generate_password():
    length = int (input("enter the desired password length:").strip())
    include_uppercase= input ("include uppercase lettes (yes/no):").lower().strip()
    include_splcharacters = input ("include these special characters (yes/no):").lower().strip()
    include_digits = input ("include these digits(yes/no):").lower().strip()




    if length < 5:
        print("the password must be atleast 4 characters long")
        return
    

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    special = string.punctuation if include_splcharacters == "yes" else ""
    all_characters = lower + upper + digits +special



    required_characters= []
    if include_uppercase == "yes":
        required_characters.append(random.choice(upper))
    if include_splcharacters == "yes":
        required_characters.append(random.choice(special))
    if include_digits == "yes":
        required_characters.append(random.choice(digits))
    
    

    required_length = length - len(required_characters)
    password = required_characters 

    for _ in range (required_length):
        characters = random.choice(all_characters)
        password.append(characters)

    random.shuffle(password)

    str_password = "".join(password)
    return str_password



password = generate_password()
print(password)
