import os
import random
import struct

from Crypto.Cipher import AES

def encryptFile(key, plainFile, cipherFile, chunkSize=64*1024):
    
    '''
    This function encrypts a file using AES(CBC mode)
    in this mode the Key must be either 16, 24 or 34 bytes long longer keys are more secure
    the chunkSize must be divisible by 16
    '''
    
    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    fileSize = os.path.getsize(plainFile)

    with open(plainFile, 'rb') as plainfile:
        with open(cipherFile, 'wb') as cipherfile:
            cipherfile.write(struct.pack('<Q', fileSize))
            cipherfile.write(iv)
            

            while True:
                chunk = plainfile.read(chunkSize)
                if len(chunk) == 0:
                    break

                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                cipherfile.write(encryptor.encrypt(chunk))
    return cipherfile

def main():

    #key = b'bdc635k2-283d-4a2c-a477-339ea866'
    
    
    key = raw_input('[*]Enter the key file: ')
    with open(key, 'rb') as secrete:
        content = secrete.read()
        encryptFile(content, 'plain.txt', 'plain.txt.enc')
        secrete.close()

#incase the file is n
if __name__ == '__main__':
    main()
