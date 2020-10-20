import random
import base64
import time

def generateKey():
    
    secreteKey = random.getrandbits(128)
    secreteKey = hex(secreteKey)
    secreteKey = list(str(secreteKey))
    secrete = secreteKey[:16]

    return ''.join(secrete).encode()
    


def saveKey(key, keyFile):
    with open(keyFile, 'wb') as secreteKey:
        secreteKey.write(key)
        secreteKey.close()

    return 0

def main():
    print("[*]Generating secrete key... ")
    time.sleep(2)
    saveKey()
    time.sleep(2)
    print("[*]Key Genrated succesfully.")

#incase the file is not called as a module
if __name__ == '__main__':
    main()



