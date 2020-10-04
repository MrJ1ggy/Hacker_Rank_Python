#A positive integer m is a prime product if it can be written as p×q, where p and q are both primes. .
#Write a Python function primeproduct(m) that takes an integer m as input and returns True if m is a prime product and False otherwise. (If m is not positive, your function should return False.)
#Here are some examples of how your function should work.
#>>> primeproduct(6)
#True

#>>> primeproduct(188)
#False

#>>> primeproduct(202)
#True


#Function to find factore of a number
def factors(n):
    factorlist = []
    for i in range(1,n+1):
        if n%i == 0:
            factorlist = factorlist + [i]
    return(factorlist)
 
 #Function to find if a number is prime or not
def isprime(n):
    return(factors(n)==[1,n])
  
 #Function to find if a number is a product of 2 primes or not 
def primeproduct(m):
    factorm=factors(m)
    listprime=[]
    for i in range(0,len(factorm)):
        if isprime(factorm[i]):
            listprime = listprime + [factorm[i]]
    if len(listprime)<2:
        return False
    else:
        for j in range(0,len(listprime)):
            for k in range(1,len(listprime)):
                if(listprime[j]*listprime[k]==m):
                    return True
