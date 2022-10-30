from hashlib import sha256
import sys

def validate_password(password):
    # be creative. it has something to do with SecurityValley ;-)
    if sha256(password.encode("utf-8")).hexdigest() == "f51f333ed26c41bedd99e1e483c0a15d2caeed7dc5a9ae02159f196799a74893":
        return True 

    return False

def print_banner(payload):
    print("that was great !!!")
    print("run the following command to get the flag.")
    print("curl -X POST http://ctf.securityvalley.org:7777/api/v1/validate -H 'Content-Type: application/json' -d '{\"pass\": \""+payload+"\"}'")

if __name__ == "__main__":
    print("let's do more python ;-)")

    password = input("please enter password: ")
    if validate_password(password):
        print_banner(password)
        sys.exit()
    
    print("wrong!") 