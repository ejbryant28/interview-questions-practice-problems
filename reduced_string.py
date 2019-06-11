# Steve has a string of lowercase characters in range ascii[‘a’..’z’]. He wants to reduce the string to its shortest length by doing a series of operations. In each operation he selects a pair of adjacent lowercase letters that match, and he deletes them. For instance, the string aab could be shortened to b in one operation.

# Steve’s task is to delete as many characters as possible using this method and print the resulting string. If the final string is empty, print Empty String


def reduced_string(input_string):

	i = 0
	while i < len(input_string) - 1 and len(input_string) > 0:
		if input_string[i] == input_string[i + 1]:
			input_string = input_string[:i] + input_string[i+2:]
			i = 0

		else:
			i += 1

	if not input_string:
		return 'Empty String'
		
	return input_string

assert(reduced_string('aaabccddd') == 'abd')
assert(reduced_string('aa') == 'Empty String')
assert(reduced_string('baab') == 'Empty String')
