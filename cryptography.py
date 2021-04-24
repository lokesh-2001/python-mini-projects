

"""from cryptography.fernet import Fernet
message = "hi there i'm Lokesh Dhingra"
key = Fernet.generate_key()
fernet = Fernet(key)
encMessage = fernet.encrypt(message.encode())
print("original string: ", message)
print("encrypted string: ", encMessage)
decMessage = fernet.decrypt(encMessage).decode()
print("decrypted string: ", decMessage)
"""
"""import rsa
publicKey, privateKey = rsa.newkeys(512)
message = "HI THERE I'M Lokesh Dhingra"
encMessage = rsa.encrypt(message.encode(),
						publicKey)
print("original string: ", message)
print("encrypted string: ", encMessage)
decMessage = rsa.decrypt(encMessage, privateKey).decode()
print("decrypted string: ", decMessage)
"""

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS = LETTERS.lower()

def encrypt(message, key):
    encrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num += key
            encrypted +=  LETTERS[num]

    return encrypted
def decrypt(message, key):

    decrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num -= key
            decrypted +=  LETTERS[num]

    return decrypted

def main():
    message = str(input('Enter your message: '))
    key = int(input('Enter your key [1 - 26]: '))
    choice = input('Encrypt or Decrypt? [E/D]: ')

    if choice.lower().startswith('e'):
        print(encrypt(message, key))
    else:
        print(decrypt(message, key))
if __name__ == '__main__':
    main()