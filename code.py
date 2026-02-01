
import random
import string
import sys


def generate_password(length: int, include_uppercase: bool, include_digits: bool, include_special: bool) -> str:
    if length < 4:
        raise ValueError("the password must be at least 4 characters long")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase else ""
    digits = string.digits if include_digits else ""
    special = string.punctuation if include_special else ""
    all_characters = lower + upper + digits + special

    if not all_characters:
        raise ValueError("no characters available to generate password")

    required_characters = []
    if include_uppercase:
        required_characters.append(random.choice(string.ascii_uppercase))
    if include_special:
        required_characters.append(random.choice(string.punctuation))
    if include_digits:
        required_characters.append(random.choice(string.digits))

    required_length = length - len(required_characters)
    password_chars = required_characters[:]

    for _ in range(required_length):
        password_chars.append(random.choice(all_characters))

    random.shuffle(password_chars)
    return "".join(password_chars)





def main():
    # Interactive prompts for user input
    def prompt_yes_no(prompt: str, default: bool = False) -> bool:
        suffix = " [Y/n]: " if default else " [y/N]: "
        while True:
            ans = input(prompt + suffix).strip().lower()
            if ans == "":
                return default
            if ans in ("y", "yes"):
                return True
            if ans in ("n", "no"):
                return False
            print("Please enter 'y' or 'n'.")

    def prompt_int(prompt: str, min_value: int = None, default: int = None) -> int:
        while True:
            val = input(prompt + (f" (default {default})" if default is not None else "") + ": ").strip()
            if val == "" and default is not None:
                return default
            try:
                n = int(val)
            except ValueError:
                print("Please enter a valid integer.")
                continue
            if min_value is not None and n < min_value:
                print(f"Please enter a number >= {min_value}.")
                continue
            return n

    print("Random password generator — interactive mode")
    length = prompt_int("Password length (min 4)", min_value=4, default=12)
    include_uppercase = prompt_yes_no("Include uppercase letters?", default=False)
    include_digits = prompt_yes_no("Include digits?", default=False)
    include_special = prompt_yes_no("Include special characters?", default=False)
    number = prompt_int("How many passwords to generate", min_value=1, default=1)

    try:
        for _ in range(number):
            pwd = generate_password(length, include_uppercase, include_digits, include_special)
            print(pwd)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
