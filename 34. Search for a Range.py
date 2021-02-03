# -*- encoding: utf8 -*-
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_len = len(nums)
        result_list = [nums_len, -1]
        if nums_len == 0:
            return [-1, -1]

        self.search(target, 0, nums_len - 1, result_list, nums)
        if len(result_list) == 0:
            result_list = [-1, -1]

        if result_list[0] > result_list[1]:
            result_list[0] = -1
        return result_list

    def search(self, target, left, right, result_list, nums):
        if left > right:
            return
        middle = left + (right - left) / 2

        if nums[middle] == target:
            if middle < result_list[0]:
                result_list[0] = middle
                self.search(target, left, middle - 1, result_list, nums)
            if middle > result_list[-1]:
                result_list[-1] = middle
                self.search(target, middle + 1, right, result_list, nums)

        elif nums[middle] < target:
            self.search(target, middle + 1, right, result_list, nums)
        elif nums[middle] > target:
            self.search(target, left, middle - 1, result_list, nums)

obj = Solution()
data = [5, 7, 7, 8, 8, 10]
print obj.searchRange(data, 7)


