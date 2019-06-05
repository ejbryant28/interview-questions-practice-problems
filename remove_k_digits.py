
def remove_k_digit(num, k):

	nums = list(num)

	nums.sort()

	print(nums)

	end = len(nums)-k

	nums = nums[:end]

	num_set = set(nums)

	result = ''
	for n in num:
		if n in num_set:
			result += n

	return result


print(remove_k_digit('51234512345', 5))