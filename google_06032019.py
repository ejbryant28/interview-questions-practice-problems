# Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).

from random import sample

def generate_num(n, l):

	nums = set(range(0, n))
	nums = nums - set(l)
	num = sample(nums, 1)
	return num[0]


print(generate_num(10, [1, 3, 6, 8, 2]))