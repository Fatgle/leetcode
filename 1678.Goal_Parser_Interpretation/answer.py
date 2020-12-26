class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        res = ""
        idx = 0
        while idx < len(command):
            if command[idx] == '(':
                if command[idx+1] == ')':
                    res += "o"
                    idx += 1
                else:
                    res += "al"
                    idx += 3
            else:         
                res += "G"
            idx += 1
        return res
            
