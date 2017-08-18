# This function is used to calculate n ^ power

def PowerFunc(n, power):
    if power <= 1:
        return n
    elif power % 2 == 0:
        return PowerFunc(n, power/2) * PowerFunc(n, power/2)
    else:
        return PowerFunc(n, power/2) * PowerFunc(n, power - power/2)


