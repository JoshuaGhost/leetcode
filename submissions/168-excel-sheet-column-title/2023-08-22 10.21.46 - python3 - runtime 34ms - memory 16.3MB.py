class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        cn = columnNumber
        res = ''
        while cn:
            res += chr((cn - 1) % 26 + ord('A'))
            cn = (cn - 1) // 26
        return res[::-1]