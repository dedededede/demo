class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        result = []
        min = 0
        arr.sort()
        for indexi in range(len(arr) - 1):
            i, j = arr[indexi], arr[indexi + 1]
            temp_min = abs(i - j)
            if result:
                if temp_min < min:
                    result = []
                    min = temp_min
                    result.append([i, j])
                elif temp_min == min:
                    result.append([i, j])
            else:
                min = temp_min
                result.append([i, j])
        return result

obj = Solution()
list =  [3,8,-10,23,19,-4,-14,27]
print obj.minimumAbsDifference(list)





