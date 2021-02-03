
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNodeObj(object):
    def __init__(self, x):
        self.head = ListNode(x)

    def insert(self, y):
        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(y)


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dump = ListNode(0)
        dump.next = head

        length = 0
        while head is not None:
            head = head.next
            length += 1

        length = length - n
        head = dump
        while length > 0:
            length -= 1
            head = head.next
        head.next = head.next.next
        return dump.next


obj = ListNodeObj(4)
obj.insert(5)
obj.insert(6)
obj.insert(7)

a = Solution()
a.removeNthFromEnd(obj, 3)