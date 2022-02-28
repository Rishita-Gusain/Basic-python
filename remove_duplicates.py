class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        if(len(nums)==0):
            return 0
        for j in range(i,len(nums)):
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
                
        return i+1