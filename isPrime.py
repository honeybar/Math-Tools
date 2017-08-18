def isPrime(n):
    n = abs(n)  # make n an absolute value

    if n == 1:  # check if n is 1
        return False
    elif n %  2 == 0:  # check if n is 2
        return False

    prime = True

    limit = int(n ** 0.5)  # find square root of n
    for i in range(3, limit + 1, 2):  # finding the smallest odd factor to divide n with
        if n % i == 0:  # check if n can be divided by i with no remainder
            prime = False
            break

    return prime