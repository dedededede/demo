class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        dict = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

class Solution1(object):

    def isValid(self, str):
        dict = {"]": "[", "}": "{", ")": "("}
        stack = []
        for item in str:
            if item in dict:
                stack.append(item)
            elif item in dict.values():
                if stack != [] and dict[item] != stack.pop():
                    return False
            else:
                return False

        return stack == []


obj = Solution1()
str1 = ""
print obj.isValid(str1)


import math
math.sqrt(10)