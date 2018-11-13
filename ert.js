


function calcMaxProfits(stocks) {
	// Given a list of stock prices, find what the max profit would be


	let maxProfit = 0
	let minPrice = stocks[0]

	for (let i=0; i<stocks.length; i++) {

		minPrice = Math.min(minPrice, stocks[i]);
		
		let possibleProfit = stocks[i] - minPrice;
		maxProfit = Math.max(possibleProfit, maxProfit);
	}

	if (maxProfit === 0) {
		return null
	}
	return maxProfit
}

console.log(calcMaxProfits([10, 7, 4, 8, 12, 9])==8)
console.log(calcMaxProfits([20, 19, 18, 17, 5])==null)
console.log(calcMaxProfits([100, 20, 19, 17, 21, 15]) == 4)

function getNthItem(n, a1, a2, i=0) {
	//Given two sorted arrays, return the nth item from the merged, sorted array

	//Note: i is to keep track of the number of iterations

	//first check to see if either list is empty-- if so return the right item from other list
	if (a1.length == 0) {
		return a2[n-i-1]
	}

	if (a2.length == 0) {
		return a1[n-i-1]
	}

	// if we're on the last iteration, return the smaller first item
	if (n === i + 1) {

		if (a1[0] < a2[0]) {
			return a1[0]
		}
		return a2[0]
	}

	//if we're not there yet, call the function again with the smallest item slice off and i incremented
	if (a1[0] < a2[0]) {
		return getNthItem(n, a1.slice(1), a2, i+1)
	}
	return getNthItem(n, a1, a2.slice(1), i+1)
}

console.log(getNthItem(4, [2, 2, 5, 7, 7, 12], [3, 6, 8, 10, 13])==5)
console.log(getNthItem(6, [2, 2, 5, 7, 7, 12], [3, 6, 8, 10, 13]) ==7)
console.log(getNthItem(3, [], [1, 5, 7]) ==7)
console.log(getNthItem(3, [1, 5, 7], []) ==7)







