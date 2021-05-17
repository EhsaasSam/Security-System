import random
import string

def generate_password(length: int):
    print("Hello, Welcome to Password Generator!")
    if length<4:
        raise Exception("Do not enter a value less than 4")
    compulsary_items_list = [string.digits, string.ascii_lowercase, string.ascii_uppercase, string.punctuation]
    password_list = [random.choice(i) for i in compulsary_items_list]
    
    password_list += [random.choice(string.printable) for i in range(length - len(compulsary_items_list))]
    random.shuffle(password_list)
    return ''.join(password_list)

letters=string.ascii_letters

def encrypt(message,key):
    if key==0:
        raise Exception("Key should be more than 0.")
    encrypted=""
    for chars in message:
        if chars in letters:
            num=letters.find(chars)
            num+=key
            encrypted+=letters[num%len(letters)]
        else:
            encrypted+=chars
        
    return encrypted

def decrypt(message,key):
    if key==0:
        raise Exception("Key should be more than 0.")
    decrypted=""
    for chars in message:
        if chars in letters:
            num=letters.find(chars)
            num-=key
            decrypted+=letters[num%len(letters)]
        else:
            decrypted+=chars
    return decrypted

