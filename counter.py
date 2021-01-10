import functools

class Counter:
    
    def __init__(self, low, high, step):
        self.current = low
        self.high = high
        self.step = step
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += self.step
        return self.current - self.step
        
print(functools.reduce(lambda x,y: x+y, Counter(1,100,1)))