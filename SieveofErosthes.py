# This function uses Sieve of Erosthenes algorithm to find the list of prime number from 2 to n

def SieveofErosthenes(n):
    primelist = set([2])
    for i in range(3, n+1, 2):
        primelist.add(i)
    num = 3
    for i in range(3, n+1, 2):
        p = 3
        while num * p < n:
            prod = num * p
            if prod in primelist:
                primelist.remove(num*p)
            p+=2
        num+=2

    return primelist

