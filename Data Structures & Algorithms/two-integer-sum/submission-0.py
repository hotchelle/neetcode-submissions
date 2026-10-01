class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #save the number in a hashset with index
        # 3: 0, 4: 1
        # check if diff is in hash set the return both indexes

        hashSet = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashSet:
                return [hashSet[diff], i]
            hashSet[nums[i]] = i
