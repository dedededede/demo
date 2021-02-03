class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict:
            return False
        if not s:
            return False


        for item in wordDict:
            s = s.replace(item, "")
            if not s:
                return True
        if s:
            return False

obj = Solution()
s = "cars"
wordDict = ["car","ca", "rs"]
print obj.wordBreak(s, wordDict)

