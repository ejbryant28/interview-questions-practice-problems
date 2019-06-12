# Steve has a string of lowercase characters in range ascii[‘a’..’z’]. He wants to reduce the string to its shortest length by doing a series of operations. In each operation he selects a pair of adjacent lowercase letters that match, and he deletes them. For instance, the string aab could be shortened to b in one operation.

# Steve’s task is to delete as many characters as possible using this method and print the resulting string. If the final string is empty, print Empty String


def reduced_string(s):

	i = 0
	while i < len(s) - 1 and len(s) > 0:
		if s[i] == s[i + 1]:
			s = s[:i] + s[i+2:]
			i = 0

		else:
			i += 1

	if not s:
		return 'Empty String'

	return s

assert(reduced_string('aaabccddd') == 'abd')
assert(reduced_string('aa') == 'Empty String')
assert(reduced_string('baab') == 'Empty String')

def rec_reduced_string(s, i=0):
	print(s)
	if not s:
		return "Empty String"

	if i == len(s) -1:
		return s

	if s[i] == s[i + 1]:
		return rec_reduced_string(s[:i] + s[i+2:])

	return rec_reduced_string(s, i + 1)

assert(rec_reduced_string('aaabccddd') == 'abd')
assert(rec_reduced_string('aa') == 'Empty String')
assert(rec_reduced_string('baab') == 'Empty String')
print(rec_reduced_string('acdqglrfkqyuqfjkxyqvnrtysfrzrmzlygfveulqfpdbhlqdqrrqdqlhbdpfqluevfgylzmrzrfsytrnvqyxkjfquyqkfrlacdqj'))