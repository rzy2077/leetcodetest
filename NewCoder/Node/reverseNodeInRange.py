class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        interval = n - m
        head1 = head
        head2 = head.next
        head3 = head
        head4 = head
        for _ in range(m - 1):
            head2 = head2.next
            head1 = head1.next
        for _ in range(n):
            head3 = head3.next
        for _ in range(m - 2):
            head4 = head4.next
        # print(head1.val)
        # print(head2.val)
        # print(head3.val)
        # print(head4.val)
        head1.next = head3  # 倒换后的最后node后接最后的 node
        for _ in range(interval):
            # print(f'head2.val {head2.val}')
            temp = head2.next
            head2.next = head1

            head1 = head2
            head2 = temp
        # print(head1.val)
        head4.next = head1  # 首node后接倒换后的 node
        return head

    def reverseBetween2(self, head: ListNode, m: int, n: int) -> ListNode:
        first = ListNode(next=head)
        head1 = ListNode(next=head)
        for  _ in range(m - 1 ):
             first = first.next  # first倒换的前一个结点
        print(first.val)
        pre = first
        cur = first.next  # 倒换的第一个结点
        for _ in range(m, n):
            temp = cur.next
            cur.next = pre # cur 下次记录断裂
            pre = cur   # 刷新pre为当前节点
            cur = temp
        a = first.next
        first.next = pre
        a.next = cur
        return head1


