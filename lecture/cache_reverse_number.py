# reverse the number 
# so 1110001100 becomes 0011000111
# num_reverse(123) -> 321

""" # for cache buit in advance, it is called a "lookup" table
def build_lookup_table():
    for i in range(10000):
        cache[i] = num_reverse(i)
"""

class NumReverse:
    def __init__(self):
        self.cache = {}

        # option: to initalize cache 
        for i in range(10000):
            self.cache[i] = self.num_reverse(i)

    def num_reverse(self, n):
        if n in self.cache:
            print('Cache hit')
            return self.cache[n]
        # otherwise not in cache, create reversed number
        # convert number to string, and seperated
        
        n = list(str(n))
        n.reverse()
        n = ''.join(n)
        self.cache[n] = int(n)
        return self.cache[n]

# build_lookup_table()
nr = NumReverse()

print(nr.num_reverse(123))
print(nr.num_reverse(1234))
print(nr.num_reverse(1235))
print(nr.num_reverse(12356))
