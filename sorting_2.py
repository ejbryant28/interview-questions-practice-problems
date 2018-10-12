

def bubble_sort(num_list):


	for i in range(len(num_list)-1):
		for j in range(len(num_list)-1-i):
			if num_list[j] > num_list[j+1]:
				num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

	return num_list

assert(bubble_sort([40, 3, 2, 8, 7])==[2, 3, 7, 8, 40])


def quick_sort(num_list):

	# print('num list is currently', num_list)
	if len(num_list) <= 1:

		return num_list

	mid = len(num_list)//2
	pivot = num_list[mid]

	bigger, smaller, eq = [], [], []

	for num in num_list:
		if num == pivot:
			eq.append(num)

		elif num < pivot:
			smaller.append(num)

		elif num > pivot:
			bigger.append(num)

	# print('about to call again on smaller, eq, and bigger respectively', smaller, eq, bigger)

	return quick_sort(smaller) + eq + quick_sort(bigger)

assert(quick_sort([40, 3, 2, 8, 7])==[2, 3, 7, 8, 40])


def make_merge_iter(lst_1, lst_2):

	result = []

	while lst_1 or lst_2:
		if not lst_2:
			result.extend(lst_1)
			break

		elif not lst_1:
			result.extend(lst_2)
			break

		elif lst_1[0] <= lst_2[0]:
			result.append(lst_1[0])
			lst_1 = lst_1[1:]

		else:
			result.append(lst_2[0])
			lst_2 = lst_2[1:]

	return result

assert(make_merge_iter([1, 2], [-4, 3]) == [-4, 1, 2, 3])

def make_merge(lst_1, lst_2):

	if not lst_2:
		return lst_1

	elif not lst_1:
		return lst_2

	elif lst_1[0] <= lst_2[0]:
		
		return [lst_1[0]] + make_merge(lst_1[1:], lst_2)

	elif lst_1[0] > lst_2[0]:

		return [lst_2[0]] + make_merge(lst_1, lst_2[1:])


assert(make_merge([1, 2], [-4, 3]) == [-4, 1, 2, 3])

def merge_sort(num_list):
	
	if len(num_list) <= 1:
		return num_list

	mid = len(num_list)//2
	first = merge_sort(num_list[:mid])
	second = merge_sort(num_list[mid:])

	return make_merge(first, second)

assert(merge_sort([40, 3, 2, 8, 7]) == [2, 3, 7, 8, 40])




print('passed!')
