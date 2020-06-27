import os

def openDir():

    directory = input('[*]Enter Directory to decrypt: ')
    print('decrypting files in {}'.format(directory))

    #password = input('[+]Enter the passphrase used when generating privatekey: ')
    for files in os.listdir(directory):
        fullpath = os.path.join(directory, files)
        os.system('openssl smime -decrypt -binary -in {} -inform DER -out decrypted -inkey privateKey.pem'.format(fullpath))

def decryptFile():
    encryptedFile = input('[+]Enter the file to decrypt: ')
    saveMe = input('[+]Enter the file to save the decrypted file: ')
    os.system('openssl smime -decrypt -binary -in {} -inform DER -out {} -inkey privateKey.pem'.format(encryptedFile, saveMe))

def main():
    decryptFile()

if __name__ == '__main__':
    main()
