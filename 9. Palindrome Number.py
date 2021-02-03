class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True

        length = len(str(x))
        if length == 1 or length == 0:
            return True

        return self.func(x, 1, length)

    def func(self, num, low, high):

        if low == 1:
            low_data = num / 1 % 10
        else:
            low_data = num / 10 ** (low - 1) % 10

        high_data = num / 10 ** (high - 1) % 10

        if high_data == low_data:

            if low >= high:
                return True

            return self.func(num, low + 1, high - 1)
        else:
            return False

obj = Solution()
print obj.isPalindrome(1000021)
