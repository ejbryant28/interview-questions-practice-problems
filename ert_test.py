
def calc_max_profits_1(stock_prices):
    
    #initialize buy and sell times to be first items
    sell = stock_prices[0]
    buy = stock_prices[0]

    #initialize gains to be 0.. if there is no possible gain you don't want to buy 
    gains = 0

    for i, first in enumerate(stock_prices):

    	for j in range(i+1, len(stock_prices)):

    		if stock_prices[j] - first > gains:
    			sell = stock_prices[j]
    			buy = first
    			gains = sell - buy

    #the directions don't specify this, but i think it'd be helpful. If there are no possible gains, I'm returning None.
    if not gains:
    	return None

    return gains

#given test case
assert(calc_max_profits_1([10, 7, 4, 8, 12, 9]) == 8)
# #test case where there's no possible gains
assert(calc_max_profits_1([20, 19, 18, 17, 5]) == None)
#test case where the buy and sell times aren't the overall min and max
assert(calc_max_profits_1([100, 20, 19, 17, 21, 15]) == 4)


def calc_max_profits_2(prices):

    if not prices:
        return None

    max_profit = 0
    min_price = prices[0]
    
    for price in prices:
    	#check to see if current is lower
        min_price = min(min_price, price)

        #check to see if there's a better gain
        temp_profit = price - min_price
        max_profit = max(max_profit, temp_profit)

    if not max_profit:
    	return None

    return max_profit


#given test case
assert(calc_max_profits_2([10, 7, 4, 8, 12, 9]) == 8)
# #test case where there's no possible gains
assert(calc_max_profits_2([20, 19, 18, 17, 5]) == None)
#test case where the buy and sell times aren't the overall min and max
assert(calc_max_profits_2([100, 20, 19, 17, 21, 15]) == 4)


def merge_sort(lst_1, lst_2):

	if not lst_1:

		return lst_2

	if not lst_2:

		return lst_1

	if lst_1[0] <= lst_2[0]:
		
		return [lst_1[0]] + merge_sort(lst_1[1:], lst_2)

	if lst_1[0] > lst_2[0]:

		return [lst_2[0]] + merge_sort(lst_1, lst_2[1:])


def get_nth_item(n, lst_1, lst_2):

	s_list = merge_sort(lst_1, lst_2)

	if not s_list:
		return None

	return s_list[n-1]

assert(get_nth_item(4, [2, 2, 5, 7, 7, 12], [3, 6, 8, 10, 13])==5)
assert(get_nth_item(6, [2, 2, 5, 7, 7, 12], [3, 6, 8, 10, 13])==7)

assert(get_nth_item(3, [], [1, 5, 7]) == 7)
assert(get_nth_item(4, [], []) == None)


def merge_sort_optimized(n, lst_1, lst_2, l=0):

	if l == n:
		return []

	if not lst_1:

		return lst_2[:n-l+1]

	if not lst_2:

		return lst_1[:n-l+1]

	if lst_1[0] <= lst_2[0]:
		
		return [lst_1[0]] + merge_sort_optimized(n, lst_1[1:], lst_2, l+1)

	if lst_1[0] > lst_2[0]:

		return [lst_2[0]] + merge_sort_optimized(n, lst_1, lst_2[1:], l+1)

def get_nth_item_optimized(n, lst_1, lst_2):

	s_list = merge_sort_optimized(n, lst_1, lst_2)
	if not s_list:
		return None
	return s_list[-1]

assert(get_nth_item_optimized(4, [2, 2, 5, 7, 7, 12], [3, 6, 8, 10, 13])==5)
assert(get_nth_item_optimized(6, [2, 2, 5, 7, 7, 12], [3, 6, 8, 10, 13])==7)

assert(get_nth_item_optimized(3, [], [1, 5, 7]) == 7)
assert(get_nth_item_optimized(4, [], []) == None)



