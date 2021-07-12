// 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
// Find the sum of all numbers which are equal to the sum of the factorial of their digits.
// Note: As 1! = 1 and 2! = 2 are not sums they are not included.

const factorial = (num) => {
	return (num === 1 || num === 0) 
		? 1
		: num * factorial (num - 1)
}


const isFactorion = (num) => {
	if (num === 2 || num === 1) {
		return false
	} else {
		let fact = String(num).split('').reduce((accum, curr) => {
			return accum + factorial(Number(curr))
		}, 0)
		return (fact === num)
			? true
			: false
	}
}


const sumOfFactorions = (limit) => {
	let accum = 0
	for (let i=0; i < limit; i++) {
		if (isFactorion(i)) {
			accum += i 
		}
	}
	return accum
}

console.log(sumOfFactorions(100000));