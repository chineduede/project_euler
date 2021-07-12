// Let d(n) be defined as the sum of proper divisors of n (numbers less than n
// which divide evenly into n).

// If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
// each of a and b are called amicable numbers.

// For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
// and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
// and 142; so d(284) = 220.

// Evaluate the sum of all the amicable numbers under 10000.


function factors_accum(num) {
	let accum = 0; let i = 1
	let div = num / 2
	while (i <= div) {
		if (num % i === 0) {
			accum += i
		}
		i++
	}
	return accum
}


function main() {
	let accum = 0; let flags = []
	for (let i=1; i < 10001; i++) {
		if (!flags.includes(i)) {
			let factor = factors_accum(i)
			j = factors_accum(factor)
			if (i === j && i !== factor) {
				accum += (i + factor)
				flags.push(factor)
			}
		}
	}
	return accum
}

console.log(main());