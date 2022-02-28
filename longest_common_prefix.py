class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length_strs=len(strs)
        j=strs[0]
        if(strs==None):
            return ""
        for i in strs[1:]:
            while (i[0:len(j)] != j and j):
                j = j[:len(j)-1]
 
        result = j
        return result
        