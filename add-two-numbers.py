# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class ListNodeOp(object):
    def __init__(self, x):
        self.root = ListNode(x)

    def insert(self, y):
        temp = self.root
        while temp.next is not None:
            temp = temp.next

        temp.next = ListNode(y)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        bit = 0
        root = n = ListNode(0)

        while l1 or l2 or bit:

            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next

            bit, val = divmod(v1 + v2 + bit, 10)

            temp_sum = v1 + v2 + bit
            if temp_sum >= 10:
                bit = temp_sum / 10
                val = temp_sum % 10



            n.next = ListNode(val)
            n = n.next
        return root.next

obj = Solution()
print obj.addTwoNumbers(l1, l2)
