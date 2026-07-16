class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        level = 0

        for char in s:
            ## Check whether am I alredy inside a level ?
            # If yes, add it, then and then add the char in the ans 
            if char == "(":
                if level > 0:
                    ans += char
                
                level +=1
            
            elif char == ")":
                ## As soon as we obtain a closing bracket, we first move out of a level right, so first decrease level, then check and add (this condition is for nested brackets)
                level -= 1

                if  level > 0:
                    ans += char

        return ans