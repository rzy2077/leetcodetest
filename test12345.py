import sys

from numpy._core.strings import lower

n = int(input())
a = sys.stdin.split()
print(a)
countX = 1
for index in range(n):
    tempIndex = index + countX
    if tempIndex<= n:
        s =''
        i = 0
        s.capitalize()
        s.lower()
        temp = []
        temp.copy()