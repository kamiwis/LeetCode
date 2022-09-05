class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ""
        for i in range(len(s)):
            longest = s[i]
            for x in range(i+1, len(s)):
                if s[x] not in longest:
                    longest += s[x]
                else:
                    break
            if len(longest) > len(string):
                string = longest
        return len(string)
                