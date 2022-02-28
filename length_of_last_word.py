class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length=0
        string=s.strip()
        for i in range(len(string)):
            if string[i]==" ":
                length=0
            else:
                length+=1
        return length