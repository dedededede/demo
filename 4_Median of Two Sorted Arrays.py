
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result = self.merge_list(nums1, nums2)
        length = len(result)
        if length == 0:
            return 0

        if length % 2 == 0:
            return (result[(length - 1) / 2] + result[(length - 1) / 2 + 1]) / 2.0
        else:
            return result[((length - 1) + 1) / 2]

    def merge_list(self, nums1, nums2):
        result = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        while i < len(nums1):
            result.append(nums1[i])
            i += 1

        while j < len(nums2):
            result.append(nums2[j])
            j += 1

        return result

obj = Solution()
print obj.findMedianSortedArrays([1,2], [0, 5])



