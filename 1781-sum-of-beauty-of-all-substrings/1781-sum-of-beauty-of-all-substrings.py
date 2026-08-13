class Solution:
    def beautySum(self, s: str) -> int:
        sum = 0
        for i in range(len(s)):
            mpp = {}

            for j in range(i, len(s)):

                mpp[s[j]] = mpp.get(s[j], 0) + 1
                
                sum += (max(mpp.values()) - min(mpp.values()))

        return sum