class solution:
    def mergeSort(list):
        def ms(list, left , right):
            if  left >=  right:
                return 
            mid = left + (right-left)//2
            ms(list, left, mid)
            ms(list, mid + 1, right)
            tmp = list[left:right + 1]
            #print(f'tmp {tmp}')
            l1 = 0
            l2 = mid + 1 - left #初始化为当前一段数组的开头和结尾
            for index in range(left, right + 1):
                if l1 >=  mid + 1 - left  :
                     list[index] = tmp[l2]
                     l2 += 1
                elif l2 >= right - left + 1   or  tmp[l1] < tmp[l2]:
                    list[index] = tmp[l1]
                    l1 += 1
                else: 
                    list[index] = tmp[l2]
                    l2 += 1
        ms(list, 0 , len(list) - 1)

    if __name__ == "__main__":
        len1 = int(input())
        list =[0] * len1
        for i in range(len1):
            list[i] = int(input())
        print(list)
        mergeSort(list)
        print(list)

