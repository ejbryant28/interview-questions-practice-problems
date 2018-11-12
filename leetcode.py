

def compress(chars):
	"""
	:type chars: List[str]
	:rtype int
	"""
	if len(chars) <= 1:
		return chars

	count = 1
	j = 0

	for i in range(len(chars)-1):

		#if next char is same, count += 1
		if chars[i] == chars[i + 1]:
			count += 1

		#if the next char is different and count > 1, replace this char with count. and reset count to be 1
			#need to double check the magnitude here
		else:

			if count == 1:
				chars[j] = chars[i]
				j +=1

			else:
				#to do: account for long counts
				chars[j] = chars[i]
				chars[j+1] = str(count)
				j +=2
				count = 1

	if count == 1:
		chars[j] = chars[-1]
		j += 1
		chars = chars[:j]

	else:
		# last_count = len(chars[j:])
		chars[j] = chars[-1]
		j += 1
		chars[j] = str(count)
		j+=1
		chars = chars[:j]

	return chars

assert(compress(['a', 'a', 'b', 'b', 'c', 'c', 'c'])== ['a', '2', 'b', '2', 'c', '3'])
assert(compress(['a', 'b', 'b', 'b', 'b', 'c'])==['a', 'b', '4','c'])
assert(compress(['a']) == ['a'])
assert(compress([]) ==[])

def find_largest_product(num_list):
	"""Given a list of integers, return the largest possible product of three of them"""

	if len(num_list) < 3:
		return None

	if len(num_list) == 3:
		return num_list[0] * num_list[1] * num_list[2]

	num_list.sort()

	if num_list[0] < 0 and num_list[1] < 0:
		if abs(num_list[0]) * abs(num_list[1]) * num_list[-1] > num_list[-2] * num_list[-3] * num_list[-1]:
			return abs(num_list[0]) * abs(num_list[1]) * num_list[-1]

	return num_list[-1] * num_list[-2] * num_list[-3]


assert(find_largest_product([3, 2, 3, 1, 4, 6, 5])==120)
assert(find_largest_product([-9, 2, 1, -7, 8, 7]) ==504)
assert(find_largest_product([-1, -5, 0, -200, 1])==1000)
assert(find_largest_product([-6, -5, -4, -3, -2, -1])==-6)
assert(find_largest_product([-100, -4, 0, -500])==0)
assert(find_largest_product([0, 0, 0, 0])==0)
assert(find_largest_product([-3, -3, 2, 1])==18)
assert(find_largest_product([3, 3, 0, -1])==0)
assert(find_largest_product([-100, -100])==None)

class Node():

	def __init__(self, val):

		self.val = val
		self.left = None
		self.right = None

def find_leafs(current):

	if not current:
		return 0

	if current.right == None and current.left==None:
		return 1

	return find_leafs(current.left) + find_leafs(current.right)


def find_size(current):

	if not current:
		return 0

	if not current.left and not current.right:
		return 1

	return sum([1, find_size(current.left), find_size(current.right)])


def find_min_depth(current, depths =[]):

	#gather a list of depths from the root
	#[1, 3, 4, 5, 2]

	#if current has children, 1+call the function again on both children
	#if no children, return 1
	if not current:
		return 0

	print(current.val)

	# depths = [sum([1, find_min_depth(current.right)]), sum([1, find_min_depth(current.left)])]
	print(depths)

	depths += [sum(1, find_min_depth(current.right))]
	depths += [sum(1, find_min_depth(current.left))]

	return min(depths)






A = Node('a')
B = Node('b')
C = Node('c')
D = Node('d')
E = Node('e')
F = Node('f')
G = Node('g')
H = Node('h')

I = Node('i')
J = Node('j')
K = Node('k')
L = Node('l')
M = Node('m')
N = Node('n')

other = Node('something')

A.left = B
A.right = C
C.right = D
D.right = E
E.right = F
E.left = G
G.left = H

B.left = I
I.left = J
J.right = K
K.left = L
I.right = M
M.left = N
assert(find_leafs(A)==4)
assert(find_leafs(other) == 1)

assert(find_size(A)==14)
assert(find_size(other) == 1)

print(find_min_depth(A))


