class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(0,len(nums)):
            if(nums[i]==val):
                nums.pop(i)
                i+=1
                return nums[i]
            else:
                return -1
            
            
            