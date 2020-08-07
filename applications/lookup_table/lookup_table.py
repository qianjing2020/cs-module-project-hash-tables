# Your code here
import random 
import math

cache = {}
#??? how to create cache using two inputs x, y???
# In Python, a dict key can be any immutable type... including a tuple.

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    # // is floor division
    v //= (x + y) 
    # % is modulus
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    # if cache entry not exist:
    if (x, y) not in cache:        
        cache[(x, y)] = slowfun_too_slow(x, y)
        return cache[(x, y)]
    # else, if cache exist, return cached value
    else:
        return cache[(x, y)]


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
