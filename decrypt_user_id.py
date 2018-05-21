import sys

from aes_decrypter import AesEncrypterDecrypter

if __name__ == '__main__':
    print("Start to decrypt userId...")

    if len(sys.argv) < 2:
        raise Exception("Error args!!")

    print(sys.argv[1:])

    decrypter = AesEncrypterDecrypter(key="1234567890123456")
    decrypted_text = decrypter.decrypt(sys.argv[1])
    print(decrypted_text)
