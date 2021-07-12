# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).

# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
# and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
# and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

def factors_accum(num):
    accum, i = 0, 0         #initialize factors of num accumulator accum
    div = num / 2
    while (i := i + 1) <= div:
        if num % i == 0:            
            accum += i          #i is a factor, accumulate
    return accum


def main():
    accum, flags = 0, []        
    for i in range(1, 10001):       #for numbers below 10,000
        if i not in flags:          #its amicable partner has not been checked
            fact = factors_accum(i)     
            j = factors_accum(fact)
            if i == j and i != fact:    #numbers are amicable and not the same
                accum += (i + fact)     
                flags.append(fact)      #to flag the amicable partner
    return accum                        #of the number found


print(main())