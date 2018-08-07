import os
import sys
import datetime

def getValidInput():
	a = input()
	boolValue = False
	while boolValue == False:
		boolValue = a.isnumeric()
		if (boolValue == False):
			print("Incorrect Input Try again!")
			a = input()
	return a	

def menu():
	print ("Please enter the number of which cryptographic primitive you want to use,\n1. 3DES \n2. AES \n3. Sha-256\n4. RSA \n5. X.509 Certificates")
					
	a = getValidInput()
	if a == 1:
		print (run3DES())
	if a == 2:
		print (runAES())
	if a == 3:
		print (SHA256())
	if a == 4:
		print (RSA())
	if a == 5:
		print (DS())

def run3DES():
	from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
	from cryptography.hazmat.backends import default_backend
	backend = default_backend()
	key = os.urandom(24)
	iv = os.urandom(8)
	userinput = input("enter a message: ")
	plaintext = str.capitalize(userinput)
	plaintext = userinput.encode('utf-8')
	cipher = Cipher(algorithms.TripleDES(key), modes.CFB(iv), backend=backend)
	encryptor = cipher.encryptor()
	ct = encryptor.update(plaintext) + encryptor.finalize()
	decryptor = cipher.decryptor()
	dt = decryptor.update(ct) + decryptor.finalize()
	print ('\nThis is your cipherText: ' , ct)
	print ('\nThis is your Decrypted text: ' , dt)
	print ("\n3DES is a technology in which DES is re-used in more tech-friendly way.\nIt is used by chaining three blocks of DES all with different keys.\n3DES is slower in encryption standards because it has to preform DES three different times.\nNot only is it slower, however it also is a lot more secure because its operation requires 2^112 operations.\n")
	print ("Would you like to learn more, 1.Yes or 2.No")
	b = int(input())
	if b == 1:
		print("From the 128-bit key, Rijndael generates 10 keys of 128 bits each.\nThese keys are placed into 4x4 arrays.\nThe plain text is also divided into 4x4 arrays (128 bits each).\nEach of the 128-bit plain-text items is processed in 10 rounds (10 rounds for 128-bit- keys, 12 for 192, 14 for 256).\nAfter the 10th round the code is generated.\nEach single byte is substituted in an S box and replaced by the reciprocal on GF (2 8).\nThen a bit-wise modulo-2 matrix is applied, followed by an XOR operation with 63.\nThe lines of the matrices are sorted cyclically.\nThe columns of the matrix multiplication are interchanged on GF (2 8).\nThe subkeys of each round are subjected to an XOR operation.\n")
	if b==2 :
		print("Thanks for Learning")
	menu()
	
def runAES():
	from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
	from cryptography.hazmat.backends import default_backend
	backend = default_backend()
	key = os.urandom(32)
	iv = os.urandom(16)
	userinput = input("enter a message: ")
	plaintext = str.capitalize(userinput)
	plaintext = userinput.encode('utf-8')
	cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
	encryptor = cipher.encryptor()
	ct = encryptor.update(plaintext) + encryptor.finalize()
	decryptor = cipher.decryptor()
	dt = decryptor.update(ct) + decryptor.finalize()
	print (ct)
	print (dt)
	print ("\nThe AES key expansion algorithm takes as input a four-word (16-byte) key and \n produces a linear array of 44 words (176 bytes). This is sufficient to provide a four word \n round key for the initial AddRoundKey stage and each of the 10 rounds of the cipher. \n")
	print ("Would you like to learn more, 1.Yes or 2.No")
	b = int(input())
	if b == 1:
		print ("The key is copied into the first four words of the expanded key. \n The remainder of the expanded key is filled in four words at a time. \n Each added word w [i] depends on the immediately preceding word, w [i -  1], and the word four positions back, w [i -  4].\n In three out of four cases, a simple XOR is used. For a word whose position in the w  array is a multiple of 4, a more complex function is used.")
	if b == 2:
		print ("Thank you for learning")
	menu()

def SHA256():
	from cryptography.hazmat.backends import default_backend
	from cryptography.hazmat.primitives import hashes
	digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
	
	message = input("Enter message to encrypt: ")
	messageByte = str(message).encode('utf-8')
	digest.update(messageByte)
	outputUser = digest.finalize()

	
	print ('Here is the crpyted text: ', outputUser)
	print ("\nHere is a little description about SHA-256: \n")
	print ("SHA 256 is a cryptography hash function\n. It generates a fixed-size 256-bit (32-byte) hash (one-way function that cannot be decrypted back)\n. This is one of the strongest hash functions available as of right now!")
	print ("\nWould you like to learn more, 1.Yes or 2.No")
	b = int(input())
	if b == 1:
		print("SHA-256 uses a message size less than 2^64.\nThe block size is 512.\nThe word size is 32.\nThe message digest size is 256.\nSHA 256 uses six logical functions, where each function operates on a 32-bit word.\n The result of each function is a new 32-bit size!")
	if b == 2:
		print ("Thank you for learning")
	menu()

def DS():
	from cryptography.hazmat.backends import default_backend
	from cryptography.hazmat.primitives import serialization
	from cryptography.hazmat.primitives.asymmetric import rsa
	from cryptography.hazmat.primitives import hashes
	from cryptography import x509
	from cryptography.x509.oid import NameOID
	import datetime
	
	# Generate our key
	private_key = rsa.generate_private_key(public_exponent=65537,key_size=2048,backend=default_backend())
	# Write our key to disk for safe keeping
	with open("Pkey.pem", "wb") as f:
    		f.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.TraditionalOpenSSL,encryption_algorithm=serialization.BestAvailableEncryption(b"my_passphrase"),))

	# Various details about who we are. For a self-signed certificate the
	# subject and issuer are always the same.
	subject = issuer = x509.Name([x509.NameAttribute(NameOID.COUNTRY_NAME, u"CA"),
  		 x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"ON"),
  		 x509.NameAttribute(NameOID.LOCALITY_NAME, u"Oshawa"), 
   		x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UOIT"), 
  		 x509.NameAttribute(NameOID.COMMON_NAME, u"uoit.ca/prof_martin"),])
	cert = x509.CertificateBuilder().subject_name(
    		subject
	).issuer_name(
    		issuer
	).public_key(
    		private_key.public_key()
	).serial_number(
    		555333
	).not_valid_before(
    		datetime.datetime.utcnow()
	).not_valid_after(
    		# Our certificate will be valid for 10 days
    		datetime.datetime.utcnow() + datetime.timedelta(days=10)
	).add_extension(
   		 x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
    		critical=False,
	# Sign our certificate with our private key
	).sign(private_key, hashes.SHA256(), default_backend())
	# Write our certificate out to disk.
	with open("CERT.pem", "wb") as f:
    		f.write(cert.public_bytes(serialization.Encoding.PEM))
	print ("\nWould you like to learn more, 1.Yes or 2.No")
	b = int(input())
	if b == 1:
		print("Digital certifications ensure information is all correctly identified, and prevents forgery of information. THey are given out by trusted agencies and ensures that all information works in conjucntion and everything matches such as private and public key, and digital signatures. The most common certificate used is X.509 and it includes version, serial number, algorithm information, valifiity, period of the certificate, etc...")
	if b == 2:
		print ("Thank you for learning")
	menu()


def RSA():
	from cryptography.hazmat.backends import default_backend
	from cryptography.hazmat.primitives.asymmetric import rsa
	from cryptography.hazmat.primitives import hashes
	from cryptography.hazmat.primitives.asymmetric import padding

	#key generation
	private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048,   backend=default_backend()  )

	#encryption
	public_key = private_key.public_key()
	userinput = input("enter a message: ")
	plaintextt = str.capitalize(userinput)
	plaintextt = userinput.encode('utf-8')
	print("\nthis is your plain text: ")
	print (plaintextt)
	ciphertext = public_key.encrypt(plaintextt, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA1()),     algorithm=hashes.SHA1(), label=None) )
	print("\nThis is your Ciphertext: ")
	print(ciphertext)

	#decryption
	plaintext = private_key.decrypt(ciphertext, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA1()),         algorithm=hashes.SHA1(), label=None))
	print('Successful decryption:', plaintext == plaintextt)
	print('Bytes in ciphertect:', len(ciphertext))
	print("\nThis is your private key: ")
	print(private_key)
	
	#explanation
	print ("\nThe RSA  scheme is a cipher in which the plaintext and ciphertext are integers between 0 and n -  1 for some n \nA typical size for n  is 1024 bits, or 309 decimal digits.\nThat is, n  is less than 21024. \n")
	print ("\nWould you like to learn more, 1.Yes or 2.No")
	b = int(input())
	if b == 1:
		print ("RSA makes use of an expression with exponentials.\nPlaintext is encrypted in blocks, with each block having a binary value less than some number n.\nThat is, the block size must be less than or equal to log2 (n ) +  1; in practice, the block size is i  bits, where 2i < n =  2i+1.\nEncryption and decryption are of the following form, for some plaintext block M  and ciphertext block C.\nC = M^e  mod n\nM = C^d  mod n =  (M^e )^d  mod n = M^ed  mod n\nBoth sender and receiver must know the value of n.\nThe sender knows the value of e , and only the receiver knows the value of d.\nThus, this is a public-key encryption algorithm with a public key of PU =  {e , n } and a private key of PR =  {d , n }.")
	if b == 2:
		print ("Thank you for learning")	
	menu()



menu()


