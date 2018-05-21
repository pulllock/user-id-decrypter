import sys

from aes_decrypter import AesEncrypterDecrypter

if __name__ == '__main__':
    print("Start to encrypt userId...")

    if len(sys.argv) < 2:
        raise Exception("Error args!!")

    print(sys.argv[1:])

    encrypter = AesEncrypterDecrypter(key="1234567890123456")
    print(encrypter.encrypt(sys.argv[1]))
