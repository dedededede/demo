class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        if divisor == 0:
            return
        if dividend == divisor:
            return 1

        a = abs(dividend)
        b = abs(divisor)
        flag = dividend >> 31 ^ divisor >> 31
        if flag:
            flag = -1
        else:
            flag = 1

        result = 0
        while a >= b:
            count = 0
            while a >= b << count:
                result += 1 << count
                a -= b << count
                count += 1
        if result * flag > 2147483647:
            return 2147483647
        if result * flag < -2147483648:
            return -2147483648
        return result * flag

a = Solution()
print a.divide(-10, -1)
