#Given a sentence (string), reverse it. Preserve correct spelling and capitalization.

#first iteratively
def rev_sent(sentence):
	sentence_words = sentence.split(' ')
	new_sentence = []

	for i in range(1, len(sentence_words)+1):
		new_sentence.append(sentence_words[-i])

	return ' '.join(new_sentence)


assert rev_sent('The cat ate peanuts') == 'peanuts ate cat The'

#recursively
def rev_sent_rec(sentence):

	sentence_words = sentence.split(' ')

	if len(sentence_words) == 1:
		return sentence_words[0]

	else:
		new_string = ' '.join(sentence_words[:-1])
		return sentence_words[-1] + ' ' + rev_sent_rec(new_string)

assert rev_sent('The cat ate peanuts') == 'peanuts ate cat The'

def rev_sent_cap(sentence):
	#this time capitalize the first words and lower the last
	sentence_words = sentence.split(' ')
	new_sentence = []

	for i in range(1, len(sentence_words)+1):
		new_sentence.append(sentence_words[-i])

	new_sentence[0] = new_sentence[0].capitalize()
	new_sentence[-1] = new_sentence[-1].lower()

	return ' '.join(new_sentence)


assert rev_sent_cap('The cat ate peanuts') == 'Peanuts ate cat the'
print('passed!')