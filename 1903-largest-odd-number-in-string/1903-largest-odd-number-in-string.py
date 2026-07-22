class Solution:
    def largestOddNumber(self, num: str) -> str:
        ## just check from the very end if odd return current to first index entire value else empty

        i = len(num) - 1
        while i >= 0:
            if int(num[i]) % 2 != 0:
                return num[0 : i + 1]
            else:
                i -= 1
        return ""