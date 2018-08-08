# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os, sys

#
def decryptCipher(ciphertext):
    
    
    #n is the potential key value
    #i ist the iterator value of the length of the ciphertext
    for n in range(0, 26):
        key = n
        plainText = ''
        for i in range (0, len(ciphertext)):
            #ranges from 97 to 122
            if (ord(ciphertext[i]) - key < 97) :
                newChr = 123 - (97 - (ord(ciphertext[i]) - key))            
            else:
                newChr = ord(ciphertext[i]) - key
            plainText += chr(newChr)
            key = n
        print ("Key value " + str(n) + ":   "    + plainText)
            


#main program running here
decryptCipher('kbslrpfknrfbqbwmxpbqobebobru')
    
        
        
    