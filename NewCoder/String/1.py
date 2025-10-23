#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @param n int整型
# @return string字符串
#
class Solution:
    def trans(self , s: str, n: int) -> str:
        # write code here

        list1 = []
        s = s.split(' ')
        for x1 in s:
            #print(x1)
            result = ''
            for x in x1:
                if x.islower():
                    result += x.upper()
                else:
                    result += x.lower()
            list1.append(result)
        result = ''
        while list1:
            result += list1.pop()
            if len(list1) != 0:
                result += " "
        return result


#chr(ord(s[i]) - ord('A') + ord('a'))