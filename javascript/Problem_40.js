// An irrational decimal fraction is created by concatenating the positive integers:

// 0.123456789101112131415161718192021...

// It can be seen that the 12th digit of the fractional part is 1.
// If dn represents the nth digit of the fractional part, find the value of the following expressio

// d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

function* champernownesConst () {
	// A generator that yields the next digit of the champernownes constant
	let str = ''; let index = 0
	while (true) {
		for (let i of str) {
			yield i
		}
		index++
		str = String(index)
	}
}

function main (limit) {
	let accum = 1; let count = 0
	for (let i of champernownesConst()) {
		if (count === limit) {
			return accum
		}
		count++
		if (count === 1 || count === 10 || count === 100 || 
			count === 1000 || count === 10000 || count === 100000 ||
			count === 1000000) {
			accum *= Number(i)
		}
	}
}

console.log(main(1000001))