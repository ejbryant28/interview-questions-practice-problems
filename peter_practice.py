
# node:
	# left
	# right
	# val

#dfs:

#given a root, find the node with the biggest value, return it

# stack-- filo

# def find_biggest_node(root):

# 	# to_see
# 	# biggest = root
# 	#while 
# 	#if node > biggest
# 		# reset biggest

# 	# add kids to to_see

# 	#return biggest

# 	pass

def find_biggest_node(current):

	#base: i am done traversing
	if not current:
		return []

	if not current.val:
		return 'no value'

	# if there's no kids- return value of node
	if not current.left or current.right:
		return current.val

	# if there are kids, return value of node and call find_biggest on kids

	return max([current.val] + [find_biggest_node(current.left)] + [find_biggest_node(current.right)])



# given a list of lamp coordinates, a list of query coordinates, and the size of the matrix

