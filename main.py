def password_menu():
    from pw_generator import generate_password
    length = int(input("Enter length of password: "))
    password = generate_password(length)
    print("Your password is: ",password)

def enc_decrypt_menu():
    from pw_generator import encrypt
    from pw_generator import decrypt
    message=input("Enter your message: ")
    key=int(input("Enter your key (1-26): "))
    choice=input("Encrypt or Decrypt? (E/D): ")

    if choice.lower().startswith('e'):
        print("Encrypted message: ", encrypt(message,key))
    elif choice.lower().startswith('d'):
        print("Decrypted message: ", decrypt(message,key))

print("\nHello, Welcome to Security System!")
def main():
    
    choice = input("\nEnter choice: \n1. Generate Password\n2.Encrypt/Decrypt\n3.Exit:\n")
    if choice == '1':
        try:
            password_menu()
        except Exception as e:
            print(e)
    elif choice == '2':
        try:
            enc_decrypt_menu()
        except Exception as e:
            print(e)
    elif choice=='3':
        print("Thank you!")
        exit()
    
    else:
        print("Invalid choice!")
        exit()

if __name__=='__main__':
    while True:
        main()