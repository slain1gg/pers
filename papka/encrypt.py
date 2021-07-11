from cryptography.fernet import Fernet

def encrypt(filename, key):
	f = Fernet(key)

	with open(filename, 'rb') as file:
		file_data = file.read()
	
	encrypted_data = f.encrypt(file_data)

	with open(filename, 'wb') as file:
		file.write(encrypted_data)

key = "gmkO7tQ-uMl9niqAsaNZ1FPCPhZJrwoVmRCG8KTPltk="
file = "1.txt"

encrypt(file, key)