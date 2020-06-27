import os

def _opendir():
    directory = './rooter'

    for files in os.listdir(directory):
        filepath = os.path.join(directory, files)
        os.system(f'openssl smime -encrypt -binary -aes-256-cbc -in {filepath} -out {filepath} -outform DER certificate.pem')

def encryptFile():
    encryptMe = 
    saveMe = 
    os.system('openssl smime -encrypt -binary -aes-256-cbc -in {} -out {} -outform DER certificate.pem'.format(encryptMe, saveMe))

def main():
    encryptFile()

if __name__ == '__main__':
    main()
