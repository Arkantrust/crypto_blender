import secrets
from hashlib import sha256, sha512
from pyperclip import copy

filename = "words.txt"

with open(filename, "r") as file:
    words = [line.strip() for line in file]


def word() -> str:
    return secrets.choice(words)


symbols: list[str] = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "-",
    "_",
    "+",
    "=",
    "[",
    "]",
    "{",
    "}",
    ";",
    ":",
    "<",
    ">",
    ", ",
    ".",
    "/",
    "?",
    "|",
]


def symbol() -> str:
    return secrets.choice(symbols)


def number() -> str:
    return str(secrets.randbelow(10))


def shuffle(string: str) -> str:
    chars = list(string)
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def gen_rand_password(length: int):
    print("Generating password...")
    password = ""
    for _ in range(length):
        password += word()
        password += symbol()
        password += number()
        password = shuffle(password)
    return password[:length]


DEFAULT_PASSWORD_SIZE = 500

def gen_256_key() -> str:
    key: bytes = gen_rand_password(DEFAULT_PASSWORD_SIZE).encode()
    print("Generating 256-bit key...")
    return sha256(key).hexdigest().upper()


def gen_512_key():
    key: bytes = gen_rand_password(DEFAULT_PASSWORD_SIZE).encode()
    print("Generating 512-bit key...")
    return sha512(key).hexdigest().upper()


def to_clipboard(text):
    copy(text)


def print_menu() -> None:
    print("I need a...")
    print("1. 256-bit key")
    print("2. 512-bit key")
    print("3. Secure password")
    print("4. Exit")


if __name__ == "__main__":
    print_menu()
    choice = input("$ ")

    if choice == "1":
        key = gen_256_key()
        print(key)
        to_clipboard(key)
        print("Key hashed with SHA256 and copied to clipboard!")

    elif choice == "2":
        key = gen_512_key()
        print(key)
        to_clipboard(key)
        print("Key hashed with SHA512 and copied to clipboard!")

    elif choice == "3":
        length = int(input("How many characters? "))
        password = gen_rand_password(length)
        print(password)
        to_clipboard(password)
        print("Password copied to clipboard!")

    elif choice == "4":
        print("Goodbye!")

    else:
        print("Invalid choice")

    exit()