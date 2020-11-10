#Kinesys AES decrypt Example(key, cipher 주어진 경우).py

from Crypto.Cipher import AES

cipher = 'f9a385a21faa40ae6313d225987b87c554ca0a2e32a42a28a71c1c155ec787d76a4ea9aeb71339335747b91bd50faa99'

key = 7901925
key = str(key)

while len(key) < 32:
    key = '0' + key

c = AES.new(key, AES.MODE_ECB)

result = c.decrypt(cipher)

print result
