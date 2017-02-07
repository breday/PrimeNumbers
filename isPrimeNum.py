def isPrimeNum(n):
		for x in range(2, n+1):
			if n % x == 0 and n<2:
				print (n,'is not a prime number')
			elif n=0 and n=1:
				print(n,"Prime Number start from 2")
			else:
				 print (n,'is a prime number')
				 break

print(isPrimeNum(9))

