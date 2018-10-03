

def bubble_sort(num_list):

	for i in range(len(num_list)-1):
		for j in range(len(num_list)-1-i):

			if num_list[j+1] < num_list[j]:
				num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

	return num_list

assert(bubble_sort([1, 2, 5, -7, -4, 0])) == [-7, -4, 0, 1, 2, 5]

def merge_sort(num_list):
	""""""
	if len(num_list) <= 1:
		return num_list

	mid = len(num_list)//2

	lst_1 = merge_sort(num_list[:mid])
	lst_2 = merge_sort(num_list[mid:])

	return make_merge_rec(lst_1, lst_2)


def make_merge(lst_1, lst_2):
	
	result = []

	while lst_1 or lst_2:

		if len(lst_1) == 0:
			result.extend(lst_2)
			break
		elif len(lst_2) == 0:
			result.extend(lst_1)
			break

		elif lst_1[0] <= lst_2[0]:
			new = lst_1.pop(0)

		elif lst_2[0] < lst_1[0]:
			new = lst_2.pop(0)

		result.append(new)
	return result

def make_merge_rec(lst_1, lst_2):

	if not lst_1:

		return lst_2

	if not lst_2:

		return lst_1

	if lst_1[0] <= lst_2[0]:
		
		return [lst_1[0]] + make_merge_rec(lst_1[1:], lst_2)

	if lst_1[0] > lst_2[0]:

		return [lst_2[0]] + make_merge_rec(lst_1, lst_2[1:])



assert(merge_sort([1, 2, 5, -7, -4, 0])) == [-7, -4, 0, 1, 2, 5]


def quick_sort(num_list):

	if not num_list:
		return []
	
	mid = len(num_list)//2
	pivot = num_list[mid]

	hi, lo, eq = [], [], []

	for num in num_list:
		if num < pivot:
			lo.append(num)
		if num > pivot:
			hi.append(num)
		if num == pivot:
			eq.append(num)

	return quick_sort(lo) + eq  + quick_sort(hi)



assert(quick_sort([1, 2, 5, -7, -4, 0])) == [-7, -4, 0, 1, 2, 5]



print('passed!')