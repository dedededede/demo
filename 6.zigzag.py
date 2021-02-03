class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        amountInUnit = numRows + numRows - 2
        totalUnits = len(s) / amountInUnit
        if len(s) % amountInUnit != 0:
            totalUnits += 1

        rows = numRows
        cols = totalUnits * (numRows - 1)

        map = [[None for j in range(cols)] for i in range(rows)]
        i = 0
        while i < len(s):
            ch = s[i]
            unitNumber = i / amountInUnit
            posInUnit = i % amountInUnit
            x, y = 0, 0
            if posInUnit < numRows:
                x = posInUnit
                y = unitNumber * (numRows - 1)
            else:
                x = numRows - 1 - (posInUnit + 1 - numRows)
                y = numRows - x - 1 + unitNumber * (numRows - 1)

            map[x][y] = ch
            i += 1

        print map


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        result = [''] * numRows

        step = 1
        row_num = 0
        for x in s:
            result[row_num] += x
            if row_num == numRows - 1:
                step = -1
            elif row_num == 0:
                step = 1
            row_num += step
        return "".join(result)

obj = Solution()
print obj.convert('PAYPALISHIRING', 3)
