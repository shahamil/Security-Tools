# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 17:17:23 2016

@author: 100484737
"""


#AES SOURCE CODE UTILIZATION:

import os
import binascii
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()
key = os.urandom(32)
iv = os.urandom(16)

plainText = input("Please enter the message you would like to encrypt using the AES Encryption Algorithm: ")
plainText = plainText.encode("utf-8")


cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
encryptor = cipher.encryptor()
plainText = str(plainText).encode('utf-8')
ct = encryptor.update(plainText) + encryptor.finalize()

print("Here is the value of the ciphertext of your encrypted message:\n" + str(ct) + "\n")
print("Here is the value of the key used to encrypt your message:\n" + str(key) + "\n")

decryptor = cipher.decryptor()
msg = decryptor.update(ct) + decryptor.finalize()

print("Here is the decypted value of the orginal message in plaintext:")
print(msg)
