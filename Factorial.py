#This function is used to calculate factorial number. It used a divide and conquer approach

def factorial(n):
    return product(1, n)


def product(i, n):
    if n < i:
        return 1
    if n == i:
        return n
    else:
        return product(i, (n+i)/2) * product((n+i)/2+1, n)

