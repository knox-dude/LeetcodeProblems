class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        returnStr = ""
        # divmod columnNumber-1 - important to have -1. 
        while columnNumber > 26:
            mod = (columnNumber-1) % 26
            returnStr += chr(65+mod)
            columnNumber = (columnNumber-1)//26    
            
        returnStr += chr(columnNumber+64)
        print(returnStr)
        return returnStr[::-1]
