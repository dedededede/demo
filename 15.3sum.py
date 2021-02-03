class Solution(object):
    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        print nums
        if len(nums) < 4:
            return []

        if len(nums) == 4:
            if sum(nums) == target:
                return [nums]
            else:
                return []
        for i in range(len(nums) - 3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    sum1 = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum1 == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif sum1 < target:
                        left += 1
                    elif sum1 > target:
                        right -= 1

        return result

obj = Solution()
print obj.threeSum([-1,0,1,2,-1,-4], -1)
