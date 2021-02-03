class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return

        max_len = 0
        used_dict = {}
        temp = [0, 1]
        for i in range(len(s)):
            if s[i] in used_dict:
                diff = i - used_dict[s[i]]
                if diff > max_len:
                    temp = [used_dict[s[i]], i + 1]
                    max_len = diff
            else:
                used_dict[s[i]] = i

        return s[temp[0]: temp[1]]

obj = Solution()
print obj.longestPalindrome("babcbabcbaccba")