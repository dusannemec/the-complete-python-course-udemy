"""
REMEMBER

Iterator: used to get the next value.
Iterable: used to go over all the values of the iterator.
"""

class FirstHundredGenerator:
    def __init__(self):
        self.number = 0
    
    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()
    
    def __iter__(self):
        return self

    
class AnotherIterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Focus']

    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, i):
        return self.cars[i]

for car in AnotherIterable():
    print(car)


my_numbers = [x for x in [1, 2, 3, 4, 5]]
my_numbers_gen = (x for x in [1, 2, 3, 4, 5])

print(next(my_numbers_gen))