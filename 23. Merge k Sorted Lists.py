# -*- encoding: utf8 -*-
from Queue import PriorityQueue

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dump = ListNode(0)
        queue = PriorityQueue()
        for item in lists:
            while item is not None:
                queue.put(item.val)
                item = item.next

        node = dump
        while queue.qsize() > 0:
            data = queue.get()
            while node.next:
                node = node.next
            node.next = ListNode(data)

        return dump.next

a = Solution()
b = ListNode(1)
print a.mergeKLists([b, b])