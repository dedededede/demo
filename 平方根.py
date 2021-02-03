# -*- encoding: utf8 -*-
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return
        if x == 1:
            return  1

        low = 0
        last = 0
        mid = (low + x) / 2
        up = x

        while 1:
            if mid * mid > x:
                up = mid
            else:
                low = mid

            mid = (low + up) / 2
            if abs(last - mid) < 0.00000000000001:
                return mid
            last = mid


obj = Solution()
print obj.mySqrt(13)