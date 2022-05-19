import data as data
from Crypto.Cipher import AES

key = b'Sixteen byte key'

cipher = AES.new(key, AES.MODE_EAX)

nonce = cipher.nonce

ciphertext, tag = cipher.encrypt_and_digest(data)

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')
