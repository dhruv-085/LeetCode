class Solution:
    def frequencySort(self, s: str) -> str:
        freq_count = {}

        ## Storing as char -> freq
        for char in s:
            freq_count[char] = freq_count.get(char, 0) + 1
        
        ## Sorting using custom rule, based on only freq items[1]
        sorted_chars = sorted(freq_count.items(), key = lambda items: items[1], reverse = True)
        
        ans = []
        for char, freq in sorted_chars:
            ans.append(char * freq)

        return "".join(ans)
