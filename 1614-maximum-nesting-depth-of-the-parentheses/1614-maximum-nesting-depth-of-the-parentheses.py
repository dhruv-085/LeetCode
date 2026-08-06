class Solution:
    def maxDepth(self, s: str) -> int:
        level = 0
        maxLevel = 0
        for char in s:
            if char == '(':
                level += 1
                maxLevel = max(maxLevel, level)

            elif char == ')':
                level -= 1
        
        return maxLevel