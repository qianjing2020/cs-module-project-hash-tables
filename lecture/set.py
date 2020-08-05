class Set:
    def __init__(self):
        self.data = {}

    def add(self, value):
        self.data[value]= True

    def in_set(self, value):
        return value in self.data

s = Set()
s.add(2)
s.add(5)
s.add(9)
print(s.in_set(22))
print(s.in_set(9))
