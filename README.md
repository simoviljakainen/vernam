# vernam
usage: vernam.py [-h] [-k [KEY]] text

         Vernam cipher.
          ___     ___
         (o o)   (o o)
        (  V  ) (  V  ) 
       /--m-m- /--m-m-

positional arguments:
  text                  Ciphertext (Base64) or plaintext (UTF-8) to operate on.

optional arguments:
  -h, --help            show this help message and exit
  -k [KEY], --key [KEY]
                        Key (Base64) for decryption.
