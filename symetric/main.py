import decryptor
import encryptor
import keyGen

import argparse
import time
import os

from termcolor import colored

def commands():
    parser = argparse.ArgumentParser(prog="EncSymetric", usage='%(prog)s File [options]', description="Symetric encryption toolkit:")
    parser.add_argument('File' , help="file to encrypt or decrypt")
    operations  = parser.parse_args()
    
    if operations.File:
        print(colored('[INFO]', 'green'), colored('choose the mode of operation ...\n\t[1] Encrypt \n\t[2] Decrypt...', 'red'))
        operation = input(colored('[*] Prompt: ', 'red'))
        if int(operation) == 1:
            key = keyGen.generateKey()
            print(colored('[INFO]', 'green'), colored( 'Generating 32 bit secrete key...', 'red'))
            time.sleep(2)
            plainFile = operations.File
            cipherFile = plainFile + ".enc"
            print(colored('[INFO]', 'green'), colored('Loading file to encrypt...', 'red'))
            time.sleep(2)
            encryptor.encryptFile(key, plainFile, cipherFile)
            print(colored('[INFO]', 'green'), colored('Encrypting file ...', 'red'))
            time.sleep(2)
            print(colored('[INFO]', 'red'), colored('Deleting the original File', 'green'))
            os.system("rm {}".format(operations.File))
            keyFile = plainFile.split('.')[0] + '.key'
            keyGen.saveKey(key, keyFile)
            time.sleep(3)
            print(colored('[INFO]', 'green'), colored('File Encrypted succesfully.', 'red'))

        elif int(operation) == 2:
            key = input(colored('[INFO] Enter the secrete key: ', 'green'))
            time.sleep(2)
            print(colored('[INFO]', 'green'), colored('Reading keys...', 'red'))
            time.sleep(2)
            with open(key, 'rb') as secreteKey:
                content = secreteKey.read()
                cipherText = operations.File
                plain = cipherText.split('.')
                plainText = []
                plainText.append(plain[0])
                plainText.append('.')
                plainText.append(plain[1])
                plainText = ''.join(plainText)
                print(colored('[INFO]', 'green'), colored('Decrypting the file ...', 'red'))
                print(colored('[INFO]', 'red'), colored('Deleting the encrypted file', 'green'))
                decryptor.decryptCipher(content, cipherText, plainText)
                time.sleep(2)
                print(colored('[INFO]', 'green'), colored('File Decrpyted successfully.', 'red'))
                os.system('rm {}'.format(operations.File))
                time.sleep(2)

        else:
            print('[ERROR] you can only insert 1 or 2 ...')


def main():
    commands()

if __name__ == '__main__':
    main()
