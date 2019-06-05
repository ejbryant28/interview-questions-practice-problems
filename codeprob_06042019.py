# What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?
functions = []
for i in range(10):
	# functions.append(lambda : i)
	# above is the original, you need to make it a bound variable instead of unbound.
    functions.append(lambda i=i: i)

for j in functions:
	print(j())