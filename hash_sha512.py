#this script generates an encrypted password using sha512 method 
#from plain text user input
from hashlib import sha512
from getpass import getpass

print('Input your plain text password below!')
plaintext_pwd = getpass()

h = sha512()
h.update(plaintext_pwd.encode())
hash_str = h.hexdigest()
print('This is your encrypted password using sha512 method:', hash_str)
