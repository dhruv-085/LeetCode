class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        ## simply double the string, that is add the string to itself, if the reverse goal string is valid, it will always be present in the concatenated string

        double_s = s + s

        return goal in double_s 
       