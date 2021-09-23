def cipher(message, shift):
	cipher_text = ""

	for i in range(len(message)):
		char = message[i]
		cipher_text += chr(ord(char) + shift)

	return cipher_text
	
def decipher():
	decipher_text = ""

	for i in range(len(cipher_text)):
		char = cipher_text[i]
		decipher_text += chr(ord(char) - shift)

	return decipher_text

message = input("\nEnter a message: ")
shift = int(input("Enter shift: "))

cipher_text = cipher(message, shift)
print(f"\nCipher text: {cipher_text}\n")

decipher_text = decipher()
print(f"\nDecipher text: {decipher_text}\n")