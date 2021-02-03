class Solution(object):

	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		res = []
		path = []
		length = len(nums)
		used = [0] * length
		if length == 0:
			return res

		def dfs(nums, length, depth, path, used):
			if depth == length:
				res.append(path[:])
				return
			for i in range(length):
				if used[i]: continue
				path.append(nums[i])
				used[i] = 1
				dfs(nums, length, depth + 1, path, used)
				path.pop()
				used[i] = 0

		dfs(nums, length, 0, path, used)
		return  res

obj = Solution()
data = []
print obj.permute(data)




