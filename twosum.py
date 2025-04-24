class Solution(object):
    def twoSum(self, nums, target):
        length=len(nums)
        i=0
        while i < length-1:
            j=i+1
            while j < length:
                if nums[i] + nums[j] == target:
                    return [i,j]
                else:
                    j += 1
            i += 1


        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
