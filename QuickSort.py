import random


class solution:

    def quickSort(list):
        n = len(list)

        def guide(list, left, right):
            randomIndex = random.randrange(left, right + 1)
            list[randomIndex], list[left] = list[left],list[randomIndex]
            i = left
            j = right
            guard =  list[left]
            while i < j:
                while i < j and list[j] >= guard:
                    j -= 1
                while i < j and list[i] <= guard:
                    i += 1



                list[i], list[j] = list[j], list[i]
            list[left], list[i] = list[i], list[left] #最后交换定位点
            return i #  最后中点
        def qs(list , left , right):
            if left >= right:
                print('end ',list)
                return
            guard = guide(list, left, right)
            print('after guide',list)
            qs(list, left, guard - 1)
            qs(list, guard + 1, right)

        qs(list, 0 , n - 1)





    if __name__ == "__main__":
        len1 = int(input())
        list =[0] * len1
        for i in range(len1):
            list[i] = int(input())
        print(list)
        quickSort(list)
        print(list)