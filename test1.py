class solution:


    if __name__ == '__main__' :

        num1 = str(input())
        num2 = str(input())
        l1 = len(num1) - 1
        l2 = len(num2) - 1
        lastValue = 0
        result = []
        while l2 >= 0 or   l1 >= 0 or lastValue > 0:
            t1,t2 = 0,0

            if l1 >= 0:
                t1 = ord(num1[l1]) - ord('0')
            if l2 >= 0:
                t2 = ord(num2[l2]) - ord('0')

            result.append(str((t1 + t2 + lastValue) % 10))
            if (t1 + t2 + lastValue) // 10 == 0:

                lastValue = 0
            else:

                lastValue = 1


            l1 -= 1
            l2 -= 1

        print(result)
        result1 = ''
        l1 = len(result)
        for _ in range (l1):
            result1 += (result.pop())
        print(result1)