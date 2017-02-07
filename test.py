def testPrime2(n):
	if n < 2:
		return n," is not considered a prime number"

	for x in range(2, n):
		for y in range(2, x):
			if x % y == 0:
				return n," is not a prime number"
			else:
				return n," is a prime number"
				break


testPrime2(10)
print(testPrime2)

