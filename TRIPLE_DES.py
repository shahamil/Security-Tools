# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 01:09:37 2016
By: Amil Shah
Date: October 29, 2016
Description: Verifies hashes for two files
@author: 100484737
"""
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()
key = os.urandom(32)
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
encryptor = cipher.encryptor()
ct = encryptor.update(b"a secret message") + encryptor.finalize()

print(ct)

decryptor = cipher.decryptor()
msg = decryptor.update(ct) + decryptor.finalize()

print(msg)