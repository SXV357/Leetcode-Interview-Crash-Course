# 735

def asteroidCollision(asteroids: list[int]) -> list[int]:
    """
    Time complexity: O(n) amortized
    Space complexity: O(n)
    """
    stack = []
    for asteroid in asteroids:
        # this is the condition for a collision because if the previous asteroid was moving to the right and this one is moving to the left there will be a collision
        while stack and stack[-1] > 0 and asteroid < 0:
            diff = asteroid + stack[-1]
            # case 1: the magnitude of the current element is greater than the one at the top of the stack
            if diff < 0:
                stack.pop()
            # case 2: the magnitude of the current element is smaller than the one at the top of the stack
            elif diff > 0:
                asteroid = 0
            # case 3: both magnitudes are the same so both get destroyed
            else:
                asteroid = 0
                stack.pop()
        
        # the way we avoid adding the current asteroid in the situations above is setting it to 0 and then only adding the non-zero elements
        
        if asteroid:
            stack.append(asteroid)

    return stack

print(asteroidCollision([-2,1,1,-2]))
print(asteroidCollision([5,10,-5]))
print(asteroidCollision([8,-8]))
print(asteroidCollision([10,2,-5]))