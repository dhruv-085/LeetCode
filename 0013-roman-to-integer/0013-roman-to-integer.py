class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        n = len(s)
        if n == 0:
            return 0
        roman = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        ## checks till last to second char only, if last too is not speical, by default last char is always added else the answer will get subtracted, special means the roman 1 is less than roman 2
        for i in range(n - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                ans -= roman[s[i]]
            else:
                ans += roman[s[i]]
            
        ## last char always added as it has no other value to compare with 
        return ans + roman[s[-1]]
            
        return ans