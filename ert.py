


def forward_nth_item(n, lst_1, lst_2, i = 0):
	"""Given two sorted lists, return what would be the nth item in the merged, sorted list"""

	#i is keeping track of the number iteration we're on so you don't have to do any extra iterations

	#if one of the lists is empty return the correct item from the other list
	if not lst_1:
		return lst_2[n-i-1]

	elif not lst_2:
		return lst_1[n-i-1]

	#if we're on the nth iteration, return the smaller first item
	elif n == i + 1:
		if lst_1[0] < lst_2[0]:
			return lst_1[0]

		return lst_2[0]

	#if we're not to the correct item, call the function again with the smaller item sliced off and i incremented
	elif lst_1[0] <= lst_2[0]:

		return forward_nth_item(n, lst_1[1:], lst_2, i + 1)

	elif lst_1[0] > lst_2[0]:

		return forward_nth_item(n, lst_1, lst_2[1:], i + 1)



assert(forward_nth_item(4, [2, 2, 5, 7, 7, 12], [3, 6, 8, 10, 13]) ==5)
assert(forward_nth_item(6, [2, 2, 5, 7, 7, 12], [3, 6, 8, 10, 13]) ==7)
assert(forward_nth_item(3, [], [1, 5, 7]) ==7)
assert(forward_nth_item(3, [1, 5, 7], []) ==7)

def backwards_nth_item(n, lst_1, lst_2, i=0):
	"""Given two sorted lists return the nth LARGEST item from the merged, sorted list-- work from the ends"""

	#i is keeping track of iterations

	#if either list is empty, return the correct item from the other list
	if not lst_1:

		return lst_2[-n-i]

	if not lst_2:

		return lst_1[-n-i]

	#if we're on the correct iteration, return the bigger last item
	if i == n - 1:

		if lst_1[-1] > lst_2[-1]:
			return lst_1[-1]

		return lst_2[-1]


	#if we're not on the correct iteration, call the function again with the bigger last item sliced off and i incremented
	elif lst_1[-1] >= lst_2[-1]:

		return backwards_nth_item(n, lst_1[:-1], lst_2, i + 1)

	elif lst_1[-1] < lst_2[-1]:

		return backwards_nth_item(n, lst_1, lst_2[:-1], i + 1)


assert(backwards_nth_item(8, [2, 2, 5, 7, 7, 12], [3, 6, 8, 10, 13])==5)
assert(backwards_nth_item(6, [2, 2, 5, 7, 7, 12], [3, 6, 8, 10, 13])==7)
assert(backwards_nth_item(1, [], [1, 5, 7])==7)
assert(backwards_nth_item(1, [1, 5, 7], [])==7)
assert(backwards_nth_item(3, [1, 5, 7], [])==1)

def get_nth_item(n, lst_1, lst_2):
	"""Given two sorted lists, return the nth item from the merged, sorted list
	time: O(n)
	space: O(1)
	"""

	#If both lists are empty return None
	if not lst_1 and not lst_2:
		return None

	#if n is closer to the end, it'd be faster to work from the end so call backwards nth
	mid = len(lst_1) + len(lst_2) / 2
	if n > mid:

		backwards_n = len(lst_2) + len(lst_1) - n + 1
		return backwards_nth_item(backwards_n, lst_1, lst_2)

	#otherwise call forward nth item
	return forward_nth_item(n, lst_1, lst_2)




assert(get_nth_item(4, [2, 2, 5, 7, 7, 12], [3, 6, 8, 10, 13]) ==5)
assert(get_nth_item(6, [2, 2, 5, 7, 7, 12], [3, 6, 8, 10, 13]) ==7)
assert(get_nth_item(3, [], [1, 5, 7]) ==7)
assert(get_nth_item(3, [1, 5, 7], []) ==7)
assert(get_nth_item(4, [], [])== None)
