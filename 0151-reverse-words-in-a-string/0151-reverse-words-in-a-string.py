class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        i = len(s) - 1
        while i >= 0:
            ## Starting from right, if any spaces trim i.e. keep skiping
            while i >= 0 and s[i] == " ":
                i -= 1

            if i < 0:
                break
            
            end = i

            while i >= 0 and s[i] != " ":
                i -= 1
            
            word = s[i + 1 : end + 1]

            ## Before storing it just check if it is not empty, means it contains some word so before storing next word, add space
            if ans != "":
                ans += " "

            ans += word

        return ans 