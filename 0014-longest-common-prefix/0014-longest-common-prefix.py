class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()

        ## Compare only first and last strings why?
        ## Because when sorted, lexicographical sorting works in that manner that similar strings comes one after the other
        s1 = strs[0]
        s2 = strs[-1]
        
        ans = []
        for i in range(min(len(s1), len(s2))):
            if s1[i] != s2[i]:
                return ''.join(ans)

            ans.append(s1[i])

        return ''.join(ans)