class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # write code here
        def reverse(start, end):
            pre = None
            cur = start
            while pre != end:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            return end, start

        first = ListNode(0)
        guard = first
        first.next = head
        while first.next:

            end1 = first
            for _ in range(k):
                end1 = end1.next
                if not end1:
                    return guard.next
            head1 = first.next
            temp = end1.next
            # print(f'head1 {head1.val}, end1 {end1.val}, temp {temp.val}')
            head2, end2 = reverse(head1, end1)
            # print(f'head2 {head2.val}, end2 {end2.val}')
            first.next = head2
            end2.next = temp
            first = end2

        return guard.next