class Solution:
    def isValid(self, s: str) -> bool:
        valid_parentheses = [("(", ")"), ("{", "}"), ("[", "]")]
        stack = []
        
        #if length of s is not even, can't have enough characters to be valid
        if len(s) % 2 != 0:
            return False
        
        
        for c in s:
            #check if the existing item in stack is the opening bracket for the current character and remove from stack if so
            if len(stack) > 0 and (stack[-1], c) in valid_parentheses:
                stack.pop()
            #if stack is empty or the opening bracket is not in stack, add to stack
            else:
                stack.append(c)
        
        return len(stack) == 0
        
        
                
            
        