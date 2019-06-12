# Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

# For example, the given cleartext and the alphabet is rotated by . The encrypted string is

# .

# Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

# Function Description

# Complete the caesarCipher function in the editor below. It should return the encrypted string.

# caesarCipher has the following parameter(s):

#     s: a string in cleartext
#     k: an integer, the alphabet rotation factor

def encryption(k):

	alphabet = 'abcdecghijklmnopqrstuvwxyz'

	encrypted = {}

	for i in range(26):

		if k > 26:
			k = k % 26

		if i + k < 25:
			encrypted[alphabet[i]] = alphabet[i + k]

		else:
			remainder =  k + i - 26
			encrypted[alphabet[i]] = alphabet[remainder]
	return encrypted

def caesar_cipher(s, k):

	encrypted_alpha = encryption(k)
	phrase = []

	for char in s:
		if char.isalpha():
			phrase.append(encrypted_alpha[char])
		else:
			phrase.append(char)

	new_string = ''
	return new_string.join(phrase)

# print(caesar_cipher('hi', 3))

# print(caesar_cipher('www.abc.xy', 26))
print(caesar_cipher('www.abc.xy', 87))
