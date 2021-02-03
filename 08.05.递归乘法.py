class Solution(object):
    def multiply(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: int
        """
        if A == 0 or B == 0:
            return 0
        if A < 0 or B < 0:
            return

        if A >= 2**64 -1 or B >= 2**64 -1:
            return

        sum = 0
        for i in xrange(0, B):
            sum += A
        return sum

obj = Solution()
print obj.multiply(100000000000, 1000000)