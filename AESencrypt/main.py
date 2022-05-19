import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b"secret"
key = get_random_bytes(32)
cipher = AES.new(key, AES.MODE_CFB)
ct_bytes = cipher.encrypt(data)
iv = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')
result = json.dumps({'iv':iv, 'ciphertext':ct})
print(result)
print(key)
{"iv": "VoamO23kFSOZcK1O2WiCDQ==", "ciphertext": "f8jciJ8/"}

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')

