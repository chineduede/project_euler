// The sum of the squares of the first ten natural numbers is,
// 1**2 + 2**2 + ... + 10**2 = 385

// The square of the sum of the first ten natural numbers is,
// (1 + 2 + ... + 10)**2 = 55**2 = 3025$$

// Hence the difference between the sum of the squares of the first ten
// natural numbers and the square of the sum is 3025 - 385 = 2640$.

// Find the difference between the sum of the squares of the first one
// hundred natural numbers and the square of the sum.

function sumOfSquares  (number) {
	// A function for finding sum of squares in a given range
	return (number === 1)
		? 0
		: (number - 1) ** 2 + sumOfSquares(number - 1)
}

// console.log(sumOfSquares(10));

function squareOfSum (number) {
	// A function for finding square of sums in a given range
	let accum =  0
	for (let i=0; i < number; i++) {
		accum += i
	}
	return accum ** 2
}
	
function difference(number) {
	return squareOfSum(number) - sumOfSquares(number)
}

console.log(difference(101));