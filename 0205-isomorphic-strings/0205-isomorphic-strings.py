class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)

        ## For storing where it was spotted
        m1 = [0] * 256
        m2 = [0] * 256

        for i in range(n):
            ## ord() converts char to ascii value
            if m1[ord(s[i])] != m2[ord(t[i])]:   
                return False

            m1[ord(s[i])] = i + 1
            m2[ord(t[i])] = i + 1

        return True
              