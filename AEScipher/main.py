from Crypto.Cipher import AES
from Crypto.SelfTest.Hash.test_cSHAKE import tag

key = b'iN9eHSutl03HokVX0VvByTrIPn6mEVbA'

cipher = AES.new(key, AES.MODE_CFB, nonce="vzTNRIZxqSGEBski")
plaintext = cipher.decrypt("ciphertext")
try:
     cipher.verify(tag)
     print("The message is authentic:", plaintext)
 except ValueError:
     print("Key incorrect or message corrupted")

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('PyCharm')
