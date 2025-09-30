class Solution:
    def myAtoi(self, s: str) -> int:
        s1 = s.strip()
        negative = False
        if s1[0] == '-':
                s1 = s1[1:]
                negative = True
        else:
            if s1[0] == '+':
                s1 = s1[1:]
        if not s1[0].isdigit():
            return 0
        while s1[0] == '0':
            s1 = s1[1:]
        #print(s1)
        s2 = ''
        for x in s1:
            if x.isdigit():
                s2 += x
            else:
                break
        #print(s2)
        if s2 == '':
            return 0
        else:
            if negative == False:
                if int(s2) > pow(2, 31) - 1:
                    return pow(2, 31) - 1
                else:
                    return int(s2)
            else:
                if int(s2) > pow(1, 31) :
                    return -pow(1, 31)
                else:
                    return -int(s2)




if __name__ == '__main__':
        s1 = Solution()
        s2 = input()
        print(s1.myAtoi(s2))