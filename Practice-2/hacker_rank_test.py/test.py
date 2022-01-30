
from operator import index
from re import I
import re


s = 'HackerEarth-testing'
L="-"
index = None
for i in range(len(s)):
    if L ==s[i]:
        index = i
res = s[:index]
print(res)



class python:
    def __init__(self,a,b=1):
        self.a = a 
        self.b = b 
    def display(self):
        print("Hi".capitalize(format(self.a,self.b)))
obj1=python(5,10)
obj2=python(1)
obj1.c=2
obj1.display()


List = []
List.append(2)
List.append(0)
List.append(6)
for i in range(1,4):
    List.append((5))
for i in range(1,5):
    List.insert(3, 'Python')
print(List)
