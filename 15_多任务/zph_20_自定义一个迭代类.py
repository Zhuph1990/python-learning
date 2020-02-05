from collections import Iterable,Iterator
import time

class Classmate(object):
     def __init__(self):
        self.names = list()

     def add(self, item):
        self.names.append(item)

     def __iter__(self):
         return ClassIterator(self)


class ClassIterator():
    def __init__(self, obj):
        self.obj = obj
        self.current_num = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_num < len(self.obj.names):
            ret = self.obj.names[self.current_num]
            self.current_num +=1
            return ret
        else:
            raise StopIteration

classmate = Classmate()
print("判断classmate是否是可以迭代的对象" ,isinstance(classmate ,Iterable))

class_iterator = iter(classmate)
print("判断class_iterator是否是迭代器" ,isinstance(class_iterator ,Iterator))


classmate.add("messi")
classmate.add("suarez")
classmate.add("pique")
for name in classmate:
    print(name)
    time.sleep(1)
