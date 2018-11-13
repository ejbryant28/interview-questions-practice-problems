
import re

def is_valid_number(number):

	pattern = r'(\d{1})?[-.● ]?\(?(\d{3})\)?[-.● ]?[ ]?(\d{3})[-.● ]?(\d{4})'

	match = re.search(pattern, number)

	if match:
		return True
	return False


assert(is_valid_number('4159430003')==True)
assert(is_valid_number('skdl;f') == False)
assert(is_valid_number('1-415-890-8743') == True)
assert(is_valid_number('(415) 549-9456') == True)