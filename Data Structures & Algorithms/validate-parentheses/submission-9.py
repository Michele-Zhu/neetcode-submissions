class Solution():
    def __init__(self) :
        self.opening = "([{"
        self.closing = ")]}"
        self.inv_link = {cl : op for op, cl in zip(self.opening, self.closing)}

    def isValid(self, s: str) -> bool:
        stack = []
        print(self.inv_link)
        for char in s :
            print(stack)
            if char in self.opening :
                stack = stack + [char] #add the parenthesis to mem
            elif char in self.closing and len(stack)>0 :
                if stack[-1] == self.inv_link[char] :
                    stack = stack[:-1] #remove last parenthesis from memory
                else : 
                    return False
            elif char in self.closing and len(stack) == 0:
                return False
        return True and len(stack)==0
            
        