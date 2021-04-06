import secrets, base64
import argparse, textwrap

def vernam(text, key):
    return bytes([wb ^ kb for wb, kb in zip(text, key)])

def encrypt(text):
    text = bytes(text, "utf-8")
    key = [secrets.randbits(8) for _ in text]
    cipherText = vernam(text, key)

    print(
        f"{base64.b64encode(cipherText).decode()}\n"
        f"Key: {base64.b64encode(bytes(key)).decode()}\n"
    )
    
    return cipherText, bytes(key)

def decrypt(cipherText, key):
    cipherText = base64.b64decode(cipherText)
    key = base64.b64decode(key)
    text = vernam(cipherText, key)

    print(f"{text.decode()}\n")

    return text

def main():
    parser = argparse.ArgumentParser(
        prog='vernam.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
        '''
                     Vernam cipher.
            --------------------------------
                      ___     ___
                     (o o)   (o o)
                    (  V  ) (  V  ) 
                   /--m-m- /--m-m-

        ''')
    )      
    parser.add_argument(
        "-k", "--key", nargs="?", help="Key (Base64) for decryption.", default=None)
    parser.add_argument(
        "text", help="Ciphertext (Base64) or plaintext (UTF-8) to operate on.")

    arg = parser.parse_args()

    if(arg.key == None):
        encrypt(arg.text)
    else:
        decrypt(arg.text, arg.key)

if __name__ == "__main__":
    main()
