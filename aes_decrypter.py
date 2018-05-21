import base64

from Cryptodome.Cipher import AES


class AesEncrypterDecrypter:
    def __init__(self, key):
        self.key = key

    def decrypt(self, secret):
        aes = AES.new(str.encode(self.key), AES.MODE_CBC, str.encode(self.key))
        base64_decrypted = base64.b64decode(secret)
        decrypt_text = str(aes.decrypt(base64_decrypted), encoding='utf-8')
        return self.de_pad_text(decrypt_text)

    def encrypt(self, text):
        aes = AES.new(str.encode(self.key), AES.MODE_CBC, str.encode(self.key))
        encrypt_text = aes.encrypt(self.pad_text(text).encode('utf-8'))
        return str(base64.b64encode(encrypt_text), encoding='utf-8')

    @staticmethod
    def pad_text(text):
        return text + (AES.block_size - len(text) % AES.block_size) * chr(AES.block_size - len(text) % AES.block_size)

    @staticmethod
    def de_pad_text(text):
        return text[0:-ord(text[-1])]
