# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 01:45:13 2016
By: Amil Shah
Date: October 29, 2016
Description: This programs allows users to encrypt and decrypt files
@author: 100484737
"""

#Primative: Private Key Encryption - OPTION AES

import os
import sys
import binascii
import base64
import string
import smtplib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os, random, struct
from Crypto.Cipher import AES

#backend = default_backend()
#key = os.urandom(32)
#iv = os.urandom(16)

def encryptFileAES():
    
    #backend = default_backend()
    #key = os.urandom(32)
    #iv = os.urandom(16)
    
    return None

def AESFileOptions():
    print("Please state which mode you would like to use:")
    print("1 - Encrypt File")
    print("2 - Decrypt File")
    print("3 - Exit")
    
    opt = str(raw_input("Option Mode: "))
    
    if (opt == '1'):
        
        print("Please enter name and path of the file you would like to encrypt:")
        file = raw_input("File path + Name: ")
        
        print("Please enter the name of the output encrypted file")
        outFile = raw_input("Output File path + Name: ")
    
        #generates a 32 byte random private key
        key = os.urandom(32)
        
        print("Please enter the name of the private key")
        keyFile = raw_input("Private Key File Name: ")
        keyFile = keyFile + ".key"
        f = open(keyFile, "wb")
        f.write(key)
        f.close()
        
        print("Private Key File " + keyFile + " has been successfully generated")
        
        #encrypts user specified file
        encrypt_file(key, file, outFile)
        
        print("Encryption of file completed")
        
        #prompts user to enter the specified email address
        print("Please enter email address to send the private key")
        emailAdd = raw_input("Email Address: ")
        
        #Send Email
        emailHandler("globalsoftonline@gmail.com", emailAdd, keyFile)
        
        #return options menu
        os.system("clear")
        AESFileOptions()
        
        
        
    elif(opt == '2'):
        
        print("Please enter name and path of the file you would like to decrypt:")
        file = raw_input("File path + Name: ")
        
        print("Please enter the name of the output decrypted file")
        outFile = raw_input("Output File path + Name: ")
        
        #generates a 32 byte random private key
        print("Please enter the name of the file that has the stored private key")
        keyFile = raw_input("Enter File Name: ")
        key = open(keyFile, "rb").read()
         
        decrypt_file(key, file, outFile)
        
        #return to options menu
        AESFileOptions()
        
    elif(opt == '3'):
        sys.exit()
        os.system("clear")
        None
        
    else:
        print("Invalid Input")
        os.system("clear")
        AESFileOptions()
        
    
    
    
def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    """ Encrypts a file using AES (CBC mode) with the
        given key.

        key:
            The encryption key - a string that must be
            either 16, 24 or 32 bytes long. Longer keys
            are more secure.

        in_filename:
            Name of the input file

        out_filename:
            If None, '<in_filename>.enc' will be used.

        chunksize:
            Sets the size of the chunk which the function
            uses to read and encrypt the file. Larger chunk
            sizes can be faster for some files and machines.
            chunksize must be divisible by 16.
    """
    if not out_filename:
        out_filename = in_filename + '.enc'

    #iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(32))
    #mode set ECB
    iv = os.urandom(16)
    encryptor = AES.new(key, AES.MODE_ECB, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                print(chunk)
                print(type(chunk))
                if len(chunk) == 0:
                    break
                elif len(chunk) % 32 != 0:
                    chunk += ' '.encode("utf-8") * (32 - len(chunk) % 32)

                outfile.write(encryptor.encrypt(chunk))
                
def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    """ Decrypts a file using AES (ECB mode) with the
        given key. Parameters are similar to encrypt_file,
        with one difference: out_filename, if not supplied
        will be in_filename without its last extension
        (i.e. if in_filename is 'aaa.zip.enc' then
        out_filename will be 'aaa.zip')
    """
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_ECB, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)
            
def emailHandler(clientEmailAdd, senderEmailAdd, attachKeyFile):
    
    #establish connection with smptp server
    server = smtplib.SMTP('smtp.gmail.com:587')
    
    server.ehlo()
    server.starttls()    
    
    #authenticate with smtp server with client's credentials
    server.login("globalsoftonline@gmail.com", "******")
    
    #create messages
    msg = MIMEMultipart()
    msg["From"] = clientEmailAdd
    msg["To"] =  senderEmailAdd
    msg["Subject"] =  "Secure Key File Transmission"
    #msg["Body"] =  "Test body example"
    msg.preamble =  "Please find the provided key file within attachment" 
    
    #create attachment
    KeyFile = open(attachKeyFile, "rb")
    attachment = MIMEText(KeyFile.read())
    attachment.add_header('Content-Disposition', 'attachment', filename=attachKeyFile)
    KeyFile.close()
    msg.attach(attachment)
    
    
    #Creates Email Paramaters to Send along with email
    #msg = "Hello There"
    server.sendmail(clientEmailAdd, senderEmailAdd, str(msg))
    server.quit()
    

def main():    
    
    #emailHandler("hi", "hey")    
    AESFileOptions()  
    
    #use email handler to send key to the user
    #emailHandler("hi", "hey") 
    '''
   

    encKey =   os.urandom(32)          

    encrypt_file(encKey, "pic.png", "pic1.png")
    print("Encryption process finished")

    decrypt_file(encKey, "pic1.png", "pic2.png")
    print("Decryption process finishes")
    '''

if __name__ == "__main__": main()





#AESFileOptions()
