class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        len_shortest = len(min(strs, key=len))
        match = False
        for i in range(len_shortest, -1, -1):
            common_prefix = strs[0][:i]
            matches = 0
            for word in strs:
                if word[:i] == common_prefix:
                    matches += 1
                else:
                    continue
            if matches == len(strs):
                match = True
                break
        return common_prefix if match == True else ""
                    
            
                
                
            
            
        