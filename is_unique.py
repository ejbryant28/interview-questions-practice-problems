#given a string of ascii characters, write a function that returns True if all the characters are unique, and false if they are not
# don't use any built in python functions


def is_unique(word):
	if not word:
		return None

	chars_dict = {}
	for char in word:
		if char in chars_dict:
			return False 
		chars_dict[char] = 1

	return True

assert is_unique('') == None
assert is_unique('abc') == True
assert is_unique('Aab') == True
assert is_unique('aba') == False

#now try doing it without any built in data structures (can use sort function for simplicity)
def is_unique_chars(word):
	if not word:
		return None

	new_word = sorted(word)

	for i in range(len(word)):
		if i < len(word)-1:
			if new_word[i] == new_word[i+1]:
				return False
	return True

assert is_unique_chars('') == None
assert is_unique_chars('abc') == True
assert is_unique_chars('Aab') == True
assert is_unique_chars('aba') == False


#now try doing that without using a sort function
def unique_chars(word):
	if not word:
		return None

	for i in range(len(word)):
		if i >=len(word):
			# return True
			break
		for j in range(i + 1, len(word)):
			if word[i] == word[j]:
				# print('in the if and word at i is {} and word at j is {}'.format(word[i], word[j]))
				return False
	return True

assert unique_chars('') == None
assert unique_chars('abc') == True
assert unique_chars('Aab') == True
assert unique_chars('aba') == False

print('passed')