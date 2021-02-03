class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        max_len = 0
        used_dict = {}
        for i in range(len(s)):
            if s[i] in used_dict and start <= used_dict[s[i]]:
                start = used_dict[s[i]] + 1

            max_len = max(max_len, i - start + 1)
            used_dict[s[i]] = i

        return max_len

obj = Solution()
print obj.lengthOfLongestSubstring('abcabcbb')