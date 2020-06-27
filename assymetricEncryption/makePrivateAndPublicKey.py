import os

def generateKeys():
    
    print('[*]Generating keys will take some time please wait and take note of the password...\n')
    os.system('openssl genrsa -aes256 -out privateKey.pem 10240')
    while True:
        print('[*]generating public keys and certificate..\n')
        os.system('openssl rsa -in privateKey.pem -pubout -out publicKey.pem')
        os.system('openssl req -x509 -new -days 100000 -key privateKey.pem -out certificate.pem')
        break
    print('[*]keys generated successfully and saved in files.\n')

def main():
    generateKeys()

if __name__ == '__main__':
    main()
