class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.stack = []
        for item in s:
            if item == "]":
                str = []
                while 1:
                    if len(self.stack) > 0:
                        result = self.stack.pop()
                        if result == "[":
                            break
                        else:
                            str.append( result)
                    else:
                        break
                k = ''
                while 1:
                    if len(self.stack) > 0:
                        result = self.stack.pop()
                        if result.isdigit():
                            k += result
                        else:
                            self.stack.append(result)
                            break
                    else:
                        break
                str.reverse()
                self.stack.append(int(k[::-1]) * "".join(str))

            else:
                self.stack.append(item)

        return "".join(self.stack)



str1 = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
obj = Solution()
print obj.decodeString(str1)