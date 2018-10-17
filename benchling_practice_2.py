# '100 * 200 + 3 - 2'

def order_operations(num_str):

	num_list = num_str.split(' ')
	new_list = []

	num = 0
	i = 0

	while i < len(num_list):
		if num_list[i] == '*':
			new = int(num_list[i-1]) * int(num_list[i+1])
			num_list[i-1:i+2]= [new]

		elif num_list[i] == '/':
			new = int(num_list[i-1]) / int(num_list[i+1])
			num_list[i-1:i+2]= [new]
		else:
			i += 1

	num = num_list[0]
	for j, char in enumerate(num_list):
		if char == '+':
	
			num += int(num_list[j + 1])

		if num_list[j] == '-':
			num -= int(num_list[j + 1])

	return num

assert(order_operations('100 * 200 + 3 - 2')== 20001)
assert(order_operations('200 / 100 + 3 + 4 - 5') == 4)
assert(order_operations('200 * 2 / 100 + 3') == 7)

print('passed!')
