from cryptography.fernet import Fernet

def write_key():
	key = Fernet.generate_key()

	with open('key.txt', 'wb') as f:
		f.write(key)


def load_key():
	return open('key.txt', 'rb').read()


def encrypt(filename, key):
	f = Fernet(key)

	with open(filename, 'rb') as file:
		file_data = file.read()
	
	encrypted_data = f.encrypt(file_data)

	with open(filename, 'wb') as file:
		file.write(encrypted_data)

def decrypt(filename, key):
	f = Fernet(key)

	with open(filename, 'rb') as file:
		encrypted_data = file.read()

	decrypted_data = f.decrypt(encrypted_data)

	with open(filename, 'wb') as file:
		file.write(decrypted_data)


key = load_key()
file = "1.txt"

encrypt(file, key)
# decrypt(file, key)