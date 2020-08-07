"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
cache = {}

# create a cache for storing all a, b, c, d, and also give an index number
def build_cache(q):
    # keep count for the number of combinations found
    count = 0
    for a in q: 
        for b in q:
            for c in q:
                for d in q:
                    if f(a)+f(b)==f(c)-f(d):
                        if (a,b,c,d) not in cache:
                            cache[(a,b,c,d)] = []
                        count += 1
                        cache[(a,b,c,d)] = count
    return cache

results = build_cache(q)
print(results)