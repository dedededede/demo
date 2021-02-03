class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        result = []
        short_num = k
        if k <= 0:
            return result

        if shorter <= 0 or longer <= 0:
            return result

        if shorter == longer:
            if k >= shorter:
                return [k/shorter]
            else:
                return result

        while short_num >= 0:
            longer_num = k - short_num
            length = short_num * shorter + longer_num * longer
            result.append(length)
            short_num -= 1

        return result


obj = Solution()
print obj.divingBoard(2, 1118596, 979)
