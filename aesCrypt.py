#! python

import sys
sys.path.append('c:/program files/python310/lib/site-packages')
from random import Random
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class AesStringCipher:
    __charMap__ = "utf-8"
    __byteOrder__ = "little"
    __byteOrder__ = "big"
    __IVSize__ = 16
    __defKeySize__ = 128
    __KeySize__ = None
    __iv__ = None
    __key__ = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, key:str = None, keyHex:str = None, iv:bytes = None, ivInt:int = None, ivHex:str = None, keySize: int = None):
        if ((iv != None) and (ivHex != None)) or ((iv != None) and (ivInt != None)) or ((ivHex != None) and (ivInt != None)): raise Exception("Multiple IV's passed!")
        elif (ivInt != None): self.setIVInt(ivInt)
        elif (ivHex != None): self.setIVHex(ivHex)
        else: self.setIV(iv)        
        self.setKeySize(keySize)
        if ((key != None) and (keyHex != None)): raise Exception("Multiple Key's passed!")
        elif (keyHex != None): self.setKeyHex(keyHex)
        else: self.setKey(key)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(keyHex={self.getKeyHex()}, ivInt={self.getIVInt()}, keySize={self.getKeySize()})"

    def getIVSize(self):
        return self.__IVSize__

    def getIV(self, iv: bytes = None):
        if (self.__iv__ == None) and (iv == None):
            return self.setIV(r.randbytes(n=self.getIVSize()))
        elif (self.__iv__ == None):
            return self.setIV(iv)
        else:
            return self.__iv__

    def setIV(self, iv: bytes = None):
        if iv == None: self.__iv__ = iv
        else: self.__iv__ = bytes(iv)
        return self.__iv__

    def getIVInt(self):
        return int.from_bytes(self.getIV(), self.__byteOrder__)

    def setIVInt(self, iv: int = None):
        return self.setIV(int.to_bytes(iv, length=self.getIVSize(), byteorder=self.__byteOrder__))

    def getIVHex(self, iv: str = None):
        return self.getIV().hex()

    def setIVHex(self, iv: str = None):
        return self.setIV(bytes.fromhex(iv))

    def getKeySize(self, keySize: int = None):
        if (self.__KeySize__ == None) and (keySize == None):
            return self.setKeySize(self.__defKeySize__)
        elif (self.__KeySize__ == None):
            return self.setKeySize(keySize)
        else:
            return self.__KeySize__

    def setKeySize(self, keySize: int = None):
        if not (keySize in [None, 2, 4, 8, 16, 32, 64, 128]):
            raise Exception(f"Invalid keysize {keySize}!")
        if keySize == None: self.__KeySize__ = keySize
        else: self.__KeySize__ = int(keySize)
        return self.__KeySize__

    def getKey(self, key: bytes = None):
        if (self.__key__ == None) and (key == None):
            return self.setKey(hashlib.sha256(str(r.randbytes(n=self.getKeySize())).encode()).digest())
        elif (self.__key__ == None):
            return self.setKey(key)
        else:
            return self.__key__

    def setKey(self, key: bytes = None):
        if key == None: self.__key__ = key
        else: self.__key__ = bytes(key)
        return self.__key__

    def getKeyHex(self, key: str = None):
        return self.getKey().hex()

    def setKeyHex(self, key: str = None):
        return self.setKey(bytes.fromhex(key))

    def reKey(self):
        self.setKey()

    def fullReKey(self):
        self.setIV()
        self.reKey()

    def _pad(self, s:str) -> str:
        padding = (self.getKeySize() - (len(s) % self.getKeySize()))
        return s + padding * chr(padding)

    def _unpad(self, s:str) -> str:
        return s[:-ord(s[len(s)-1:])]

    def encryptStrMsgKeyIVToBytesMsgKeyIV(self, raw: str, key:bytes = None, iv: bytes = None) -> bytes:
        if iv == None: iv = self.getIV()
        if key == None: key = self.getKey()
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), default_backend())
        encryptor = cipher.encryptor()
        raw = self._pad(raw)
        return (encryptor.update(raw.encode(self.__charMap__)) + encryptor.finalize(), key, iv)

    def encryptStrMsgToBytesMsg(self, raw: str) -> bytes:
        return self.encryptStrMsgKeyIVToBytesMsgKeyIV(raw)[0]

    def decryptBytesMsgKeyIVToStr(self, enc: bytes, key: bytes = None, iv: bytes = None) -> str:
        if iv == None: iv = self.getIV()
        if key == None: key = self.getKey()
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), default_backend())
        decryptor = cipher.decryptor()
        try:
            raw = decryptor.update(enc) + decryptor.finalize()
        except TypeError:
            return enc
        try:
            raw = raw.decode(self.__charMap__)
        except UnicodeDecodeError:
            return enc
        return self._unpad(raw)

    def decryptBytesMsgToStr(self, enc: bytes) -> str:
        return self.decryptBytesMsgKeyIVToStr(enc)

    def encryptStrMsgKeyIVToHexMsgKeyIV(self, raw: str, key:bytes = None, iv: bytes = None) -> bytes:
        (enc_msg, key, iv) = self.encryptStrMsgKeyIVToBytesMsgKeyIV(raw, key, iv)
        return (enc_msg.hex(), key, iv)

    def encryptStrMsgToHexMsg(self, raw: str) -> bytes:
        return self.encryptStrMsgKeyIVToHexMsgKeyIV(raw)[0]

    def decryptHexMsgKeyIVToStr(self, enc: str, key: bytes = None, iv: bytes = None) -> str:
        try:
            return self.decryptBytesMsgKeyIVToStr(bytes.fromhex(enc), key, iv)
        except TypeError:
            return self.decryptBytesMsgKeyIVToStr(enc, key, iv)
        except  ValueError:
            return enc

    def decryptHexMsgToStr(self, enc: str) -> str:
        return self.decryptHexMsgKeyIVToStr(enc)

if __name__ == '__main__':
    r = Random()

    cipher = AesStringCipher(keySize=8)
    cipher = AesStringCipher()
    secret_msg = 'this is a super secret msg ...'

    (enc_msg, key, iv) = cipher.encryptStrMsgKeyIVToBytesMsgKeyIV(secret_msg)
    print(iv)
    print(cipher.getIVInt())
    print(cipher.setIVInt(cipher.getIVInt()))
    print(cipher.getIVInt())
    print(cipher.getIV())
    print(cipher.getIVHex())
    print(cipher.setIVHex(cipher.getIVHex()))
    print(cipher.getIVHex())
    print(cipher.getIV())
    print("--")
    print(key)
    print(cipher.getKeyHex())
    print(cipher.setKeyHex(cipher.getKeyHex()))
    print(cipher.getKeyHex())
    print(cipher.getKey())
    print("--")
    print(enc_msg)
    print(enc_msg.hex())
    print(cipher.encryptStrMsgKeyIVToHexMsgKeyIV(secret_msg)[0])


    dec_msg = cipher.decryptBytesMsgKeyIVToStr(enc_msg, key, iv)
    assert secret_msg == dec_msg
    print(dec_msg)
    dec_msg = cipher.decryptBytesMsgKeyIVToStr(enc_msg)

    assert secret_msg == dec_msg
    print(dec_msg)
    print(cipher)
    cipher.reKey()
    print(cipher)
    cipher.fullReKey()
    print(cipher)

    print(cipher.decryptBytesMsgKeyIVToStr(enc_msg, key, iv))
    print(cipher.decryptBytesMsgKeyIVToStr(enc_msg))
    print(cipher.decryptHexMsgKeyIVToStr(enc_msg))
    print(cipher.decryptHexMsgKeyIVToStr("this is a test"))
    print(cipher.decryptBytesMsgKeyIVToStr("this is a test"))

    cipher.encryptStrMsgKeyIVToHexMsgKeyIV("this is a test")
    print(cipher.decryptBytesMsgKeyIVToStr(cipher.encryptStrMsgKeyIVToHexMsgKeyIV("this is a test")[0]))
    print(cipher.decryptHexMsgKeyIVToStr(cipher.encryptStrMsgKeyIVToHexMsgKeyIV("this is a test")[0]))
