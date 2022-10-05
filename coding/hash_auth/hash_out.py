from hashlib import sha256
import sys

def validate_password(password):
    # be creative. The hash has maybe something todo with the event on thursday and friday and the location ;-) keep that in mind...
    if sha256(password.encode("utf-8")).hexdigest() == "f4ecea7b05c16d8f14b657484cc16bc5a93e059119f873bc0be9bb1b81c3a42e":
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