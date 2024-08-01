# 735

def asteroidCollision(asteroids: list[int]) -> list[int]:
    # cases for collision
        # current one is negative and previous is positive
            # both are same size(absolute value)
            # one is smaller than the others
    
    stack = []
    for asteroid in asteroids:
        while stack and stack[-1] > 0 and asteroid < 0:
            diff = asteroid + stack[-1]
            if diff < 0:
                stack.pop()
            elif diff > 0:
                asteroid = 0
            else:
                asteroid = 0
                stack.pop()
        
        if asteroid:
            stack.append(asteroid)

    return stack

print(asteroidCollision([-2,1,1,-2]))
print(asteroidCollision([5,10,-5]))
print(asteroidCollision([8,-8]))
print(asteroidCollision([10,2,-5]))