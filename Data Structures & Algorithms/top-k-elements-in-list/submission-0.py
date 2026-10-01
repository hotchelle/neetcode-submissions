class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a hashmap with all values and how often they appear
        #sort that hashmap in descending order
        #loop through and return the top k

        hashmap = {}

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 0
            hashmap[nums[i]] += 1

        # {1 :1; 2: 2; 3: 3}
        # sorth this

        sortedDescending = sorted(hashmap.items(), key = lambda item: item[1], reverse = True)
        
        output = []
        for i in range(k):
           item = sortedDescending[i]
           output.append(item[0]) #just the key

        return output