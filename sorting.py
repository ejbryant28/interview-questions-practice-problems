

def bubble_sort(num_list):

	for i in range(len(num_list)-1):
		for j in range(len(num_list)-1-i):

			if num_list[j+1] < num_list[j]:
				num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

	return num_list

assert(bubble_sort([1, 2, 5, -7, -4, 0])) == [-7, -4, 0, 1, 2, 5]

print('passed!')

def quick_sort(num_list):
	pass