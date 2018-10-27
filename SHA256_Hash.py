# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 05:11:52 2016
By: Amil Shah
Date: October 29, 2016
Description: Verifies hashes for two files
@author: 100484737
"""

import os
import binascii
import base64
import math 
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

#Primative: File Hash Verification


'''
This function represents 
'''
def SHA256FileOptions():
    
    
    print("Please state which mode you would like to use:")
    print("1 - Get SHA256 File Hash")
    print("2 - Verify Hashes of two files")
    print("3 - Exit")
    
    opt = input("Option Mode: ")

    if (opt == '1'):
        print("Please enter Path + Name of file you would like to retreive the SHA256 HASH from")
        file = input("Enter File Name: ")
        print("File: " + file)
        print("SHA256 File Hash Value: " + str(getHash(file)))
        
        
    elif (opt == '2'):
        
        print("Please enter the filenames of both files you would like their hashes")
       
        file1 = input("Enter Filename 1: ")       
        file2 = input("Enter Filename 2: ")
        
        fileHash1 = getHash(file1)
        fileHash2 = getHash(file2)
        
        if (fileHash1 == fileHash2):
            print("Both files have the same hash value")
            print("File 1 Hash: " + str(fileHash1))
            print("File 2 Hash: " + str(fileHash2))
        
        elif (getHash(file1)):
            print("These file are not the same file because they don't have the same hash value")
        
        print("File 1 Hash: " + str(fileHash1))
        print("File 2 Hash: " + str(fileHash2))
    
    elif (opt == '3'):
        None
        
    else:
        print("Invalid Input! Please enter valid mode option.")
        SHA256FileOptions()
        
    


#this method will resolve the sha hash of the associated file.
def getHash(file):
    
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    
    #reads file using the read byte mode
    with open(file, 'rb') as afile:
        
        #reads bytes from from the given file
        buffer = afile.read()
        digest.update(buffer)
        
    #computes the hash value of the bytes retreived from the file
    fileHash = digest.finalize()
    digest = None
    
    #returns the hash value of the file
    return fileHash
    
    
'''
def verifyFileHash(file1, file2):
    
    digest1 = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest2 = hashes.Hash(hashes.SHA256(), backend=default_backend())
    
    with open(file1, 'rb') as afile1:
        buf = afile1.read()
        digest1.update(buf)
        
    with open(file2, 'rb') as afile2:
        buf = afile2.read()
        digest2.update(buf)
    
    file1Hash = digest1.finalize()
    file2Hash = digest2.finalize()
    
    print(file1Hash)
    print(file2Hash)    
    
    if (file1Hash == file2Hash):
        return True
    
    else:
        return False
        

        
print(verifyFileHash("Resume.pdf", "Resume2.pdf"))
'''

#SHA256FileOptions()
