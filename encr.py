import random
import string

chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)

print(f"chars: {chars}")
print(f"key  : {keys}")

plain = input("Enter message to encrypt: ")
cipher = ""

for letter in plain:
    index = chars.index(letter)
    cipher += keys[index]

print(f"original    : {plain}")
print(f"encrypted   : {cipher}")

cipher = input("Enter message to decrypt: ")
plain  = ""

for letter in cipher:
    index = keys.index(letter)
    plain += chars[index]

print(f"encrypted   : {cipher}")
print(f"original    : {plain}")