

#import Fernat class (Fernat is a type of symmetric encryption, handles 
#key generation< encryption, decryption, and expiration)
from cryptography.fernet import Fernet

key = Fernet.generate_key()  #create key
with open("key.key", "wb") as key_file: 
    key_file.write(key) #write key to a file