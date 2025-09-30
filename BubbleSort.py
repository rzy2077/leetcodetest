
from collections import defaultdict

class solution:
    def bubllesort(list1):
        n = len(list1)
        for i in range(n - 1):
            for j in range(n - 1 - i ):
                if list1[j] > list1[j + 1]:
                    list1[j],  list1[j + 1] = list1[j + 1] ,  list1[j]
        print(list1)
    def insertSort2(list1):
        n = len(list1)
        for i in range(1, n):
            currentValue = list1[i]
            j = i - 1
            while j >= 0 and currentValue < list1[j]:
                list1[j + 1] = list1[j]
                j -= 1
            list1[j + 1] = currentValue
        print(list1)
    def insertSort(list1):
        n = len(list1)
        for i in range(1, n):
            currentValue = list1[i]
            inserted = False
            for j in range(i , 0, -1):
                if currentValue >= list1[j - 1]: #和前一个数值进行比较
                    list1[j] =  currentValue
                    inserted = True
                    break
                else:
                    list1[j] = list1[j - 1]
            if not inserted:
                list1[0] = currentValue

        print(list1)
    def selectionSort(list1):
        n = len(list1)
        for i in range(n):
            flag = i
            for j in range(i + 1, n):
                if list1[j] < list1[flag]:
                    flag = j
            list1[i] , list1[flag] = list1[flag], list1[i]
        print(list1)
    if __name__ == "__main__":
        list1 = []
        #words = input().split()
        #print(words)
        n = int(input())
        for _ in range(n):
            list1.append(int(input()))
        print(list1)
        #bubllesort(list1)
        selectionSort(list1)
        #print(list1)



