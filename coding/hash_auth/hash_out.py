from hashlib import sha256
import sys

def validate_password(password):
    if sha256(password.encode("utf-8")).hexdigest() == "f1bc1076b129ce68688f30bdf9e5a72e6460596c6a956afc96489ccf7b1f7a1e":
        return True 

    return False

def print_banner(payload):
    print("that was great !!!")
    print("run the following command to get the flag.")
    print("curl -X POST http://ctf-dlab.com:7777/api/v1/validate -H 'Content-Type: application/json' -d '{\"pass\": \""+payload+"\"}'")

if __name__ == "__main__":
    print("let's do more python ;-)")

    password = input("please enter password: ")
    if validate_password(password):
        print_banner(password)
        sys.exit()
    
    print("wrong!")
