class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    # have a set of values append it everytime you see it 
    # - if nums[i] is in set return true
    # - if you reach end of nums[i] in list then return false

        numsSet = set()
        for i in range(len(nums)):
            if nums[i] in numsSet:
                return True
            else:
                numsSet.add(nums[i])
        return False 