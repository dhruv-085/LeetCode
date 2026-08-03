from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = [0] * 26

        for i in range(len(s)):

            ## ord is oridinal function, used for getting ASCII values of characters
            freq[ord(s[i]) - ord('a')] += 1

            ## Same letter no matter where if obtained, will get reduced by one and eventually get cancelled out if present in the exact same number of times, hence handling duplicates as well
            freq[ord(t[i]) - ord('a')] -= 1

        for count in freq:
            if count != 0:
                return False
        return True