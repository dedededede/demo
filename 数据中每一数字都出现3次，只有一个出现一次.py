class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        for i in xrange(0, len(nums), 3):
            if i == len(nums) - 1:
                return nums[i]

            temp = nums[i: i + 3]
            if temp[0] & temp[1] ^ temp[2] != 0:
                return 2 * sum(set(temp)) - sum(temp)
obj = Solution()
a = [2, 2, 3, 2]
print obj.singleNumber(a)
