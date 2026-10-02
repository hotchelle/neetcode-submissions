class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #plan 
        #store all the multipled values pre fix in output array
        #get the postfix and multiply it

        res = [1] * len(nums)

        #prefix

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        #postfix
        postfix = 1
        for i in range(len(nums) -1 , -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
        