class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            ## odd length, start from same point hence, from i itself
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ## Always check if new palindrome is larger than pervious one then only update will update it
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = (r - l + 1)

                ## for growing outwards
                l -= 1
                r += 1
            
            ## For even length, smallest change ever for checking it up, initialize r with i + 1, thats it
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = (r - l + 1)

                ## for growing outwards
                l -= 1
                r += 1
        return res