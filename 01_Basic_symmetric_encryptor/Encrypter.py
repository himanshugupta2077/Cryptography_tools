import pandas as pd

encryptionkey = pd.read_csv(r"decode_key.csv", 
	sep = ',', names = ['Character', 'Byte'], header = None, skiprows = [0])

df = pd.DataFrame(data = encryptionkey)

df['Character'] = df['Character'].astype(str)
df['Byte'] = df['Byte'].astype(str)

def split(message):
	
	return [char for char in message]
def encrypt_message():
	encrypted_message = ""

	for i in range(len(message_split)):
		j = message_split[i]
		try:
			encrypted_char = encryptionkey.loc[encryptionkey['Character'] == j, 'Byte'].iloc[0]

		except:
			print('Unrecognized character')
			encrypted_char = '@@@'

		encrypted_message = encrypted_message + encrypted_char

	return encrypted_message
def decrypt_message(encrypted_message):
	decrypted_message = ''
	decrypted_char = []

	for i in range(0, len(encrypted_message), 2):
		j = encrypted_message[i:i + 2]
		index_nb = df[df.eq(j).any(1)]

		df2 = index_nb['Character'].tolist()

		s = [str(x) for x in df2]
		decrypted_char = decrypted_char + s

	decrypted_message = ''.join(decrypted_char)

	return decrypted_message

message = input('\nEnter the message to encrypt: ')

message_split = split(message)

encrypted_message = encrypt_message()

encrypted_message = str(encrypted_message)
decrypted_message = decrypt_message(encrypted_message)

print(f"\nOriginal message: {message}")
print(f"\nEncrypted message: {encrypted_message}")
print(f"\nDecrypted message: {decrypted_message}")