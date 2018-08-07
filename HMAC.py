# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 02:14:29 2016
By: Amil Shah
Date: October 29, 2016
Description: HMAC Authentication
@author: 100484737
"""
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac

key=os.urandom(32)

h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())

h.update(b"message to hash")
result = h.finalize()

print(result)
