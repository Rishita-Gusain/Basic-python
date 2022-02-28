class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        
        for i in range(0,len(nums)):
            
            if nums[i]==target:
                return i
            elif nums[0]>target:
                return 0
            elif i+1<len(nums) and nums[i]<target and nums[i+1]>target:
                return i+1
            
        return i+1
            