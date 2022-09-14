#/usr/bin/python3
from argparse import ArgumentParser
from sympy import mod_inverse, prime

def get_keys():
    p, q = prime(50), prime(60)
    n = p *q 
    phi = (p-1)*(q-1)
    e = 47

    return e, n, phi

def encrypt_msg(msg):
    e, n, _ = get_keys()
    enc_msg = [(ord(i) ** e) % n for i in msg]

    return enc_msg

def main(args):
    
    if args.mod == "enc":
        print(encrypt_msg(args.text))
        
    elif args.mod == "dec":
        pass

    else:
        print("unkown mode...")

if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-t","--text", dest="text", type=str)
    parser.add_argument("-m", "--mode", dest="mod", required=True)

    args = parser.parse_args()

    main(args)
