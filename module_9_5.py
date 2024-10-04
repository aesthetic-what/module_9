class StepValueError(ValueError):
    pass


class Iterator():
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start - step
        
        if self.step == 0:
            raise StepValueError('Шаг не может быть равен 0')        

    def __iter__(self):
        print(f'start pointer: {self.pointer}\n')
        return self
        
    def __next__(self):
        self.pointer += self.step

        if self.stop <= self.pointer and self.step < 0:
            print(f'pointer: {self.pointer}, stop: {self.stop}, start: {self.start}')
            return self.pointer

        elif self.stop >= self.pointer and self.step > 0:
            print(f'pointer: {self.pointer}, stop: {self.stop}, start: {self.start}')
            return self.pointer
        else:
            raise StopIteration()
        
        """
        Можно конечно и в одно условие все вписать, но мне так удобнее
        """




try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        #print(i, end=' ')
        print()
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print( end=' ')
print()
for i in iter3:
    print( end=' ')
print()
for i in iter4:
    print( end=' ')
print()
for i in iter5:
    print( end=' ')
print()
