
class FibIterator(object):
     def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1


     def __iter__(self):
         return self

     def __next__(self):
        if self.current_num < self.all_num:
            ret = self.a
            self.a ,self.b = self.b ,self.a + self.b

            self.current_num +=1
            return ret
        else:
            raise StopIteration

fibo = FibIterator(10)

for num in fibo:
    print(num)

print("-" * 10)

li = list(FibIterator(15))
print(li)
print("-" * 10)

tp = tuple(FibIterator(6))
print(tp)