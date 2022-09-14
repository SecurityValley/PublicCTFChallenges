#/usr/bin/python3

def read_flag_from_disk():
    with open("./challenge.txt") as flag:
        return bytes.fromhex(flag.read().strip())

def xor(flag, key):
    out = b""

    for i in range(len(flag)):
        out += bytes([flag[i] ^ key[i % len(key)]])

    return out

def main():
    
    res = xor(
        read_flag_from_disk(),
        b"0"
    )

    print(res)

if __name__ == "__main__":
    main()