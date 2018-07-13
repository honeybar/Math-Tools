# this function is used to calculate combinatoric (nCr)
# This function revolves the idea of reducing the range of the product so that it needs less calculation
# by picking which denominator should be crossed from n: r or n-r. This would depend which one is bigger

def Combinatorics(n, r):
    if r < n - r:
        prodrange = product(n-r + 1,  n)
        return prodrange/product(1, r)

    else:
        prodrange = product(r+1, n)
        return prodrange/product(1, n-r)


# find the product of certain range
def product(i, n):
    if n < i:
        return 1
    if n == i:
        return n
    else:
        return product(i, (n+i)/2) * product((n+i)/2+1, n)

