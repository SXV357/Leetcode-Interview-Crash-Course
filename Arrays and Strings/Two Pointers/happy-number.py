# 202

def digit_squares(n: int) -> int:
    """
    Calculates the sum of the squares of a digits of a given number
    """
    res = 0
    while n > 0:
        res += pow(n % 10, 2)
        n //= 10
    return res

def isHappy(n: int) -> bool:
    # If the number is already 1 we are done because the goal is to get n to equal 1 after replacing it by the sum of squares of its digits
    if n == 1:
        return True

    # The main idea is that if a number if not happy and loops infinitely, the sum of the squares of digits will eventually equal some previous value
        # the set is used to store all computed sum of squares of digits so that we can detect when an infinite cycle is taking place
    squared = set()

    while True:
        # we have reached the end goal(get n to equal 1 after all the computations)
        if n == 1:
            break
        
        # computing sum of squares of digits for the current value of n
        res = digit_squares(n)

        # if this computed value does not already exist in the set we just update the set with this value and the value of n to now point to this newly calculated value
        if res not in squared:
            squared.add(res)
            n = res
        # this value has already been computed previously and we are in an infinite loop so return right away
        else:
            return False
    
    return True

print(isHappy(19))
print(isHappy(13))
print(isHappy(4))
print(isHappy(2))