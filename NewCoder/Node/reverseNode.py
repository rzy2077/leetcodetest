class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:
        # write code here
        if not head:
            return None
        head2 = head.next
        head.next = None
        while head2 != None:
            #print(f'head.val {head.val}, head2.val {head2.val}')
            temp = head2.next
            head2.next = head
            head = head2
            head2 = temp

        return head

if  __name__ == '__main__':
    s1 = Solution()
    s1.ReverseList()