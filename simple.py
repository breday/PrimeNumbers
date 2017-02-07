def primeNum(num):
    
#0 and 1 are not prime numbers 
    if num < 2:
        print (num,"not considered a Prime number")

#number divisible by two
    elif num == 2:
        print (num,"is Prime number") 

#checks if the mod is zero to determine if items in range(2,x) are prime numbers 
    for n in range(2, num):
        if num % n ==0:
            return (num,"is not a Prime number")

        return True


    for n in range(2,num):
	    if (num % 2 == 0) or (num % 5 == 0):
	        return (n," is a Prime Number")
	        break
	

#print results
print(primeNum(28))

