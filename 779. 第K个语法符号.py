class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """

        flag = 0

        while N > 0:
            if K % 2 == 0:
                if flag == 0:
                    flag = 1
                else:
                    flag = 0

            K = (K - 1) / 2 + 1
            N -= 1

        return flag


obj = Solution()
print obj.kthGrammar(4, 5)
