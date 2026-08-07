class Solution:
    def myAtoi(self, s: str) -> int:
        ## using .lstrip() to strip leading spaces

        s = s.lstrip()

        if not s:
            return 0
            
        sign = 1
        i = 0

        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        ans = 0

        while i < len(s) and s[i].isdigit():
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