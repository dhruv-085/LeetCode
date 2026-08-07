class Solution:
    def myAtoi(self, s: str) -> int:
        ## using .lstrip() to strip leading spaces

        # s = s.lstrip()

        ## Raw logic without using extra O(n) space
        i = 0
        n = len(s)

        while i < n and s[i] == " ":
            i += 1
        
        if i == n: # means empty:
            return 0
        

        # if not s:
        #     return 0

        sign = 1

        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        ans = 0

        while i < n and s[i].isdigit():
            ans = ans * 10 + int(s[i])
            i += 1

        ## give the sign back
        ans *= sign

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if ans < INT_MIN:
            return INT_MIN

        elif ans > INT_MAX:
            return INT_MAX

        return ans