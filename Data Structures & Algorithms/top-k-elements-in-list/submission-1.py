class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      # plan is 
      # create a hashmap of all the elements with count
      # sort that in descending order
      # return the top k values from that

        unsortedCount = {}

        for num in nums:
            if num not in unsortedCount:
                unsortedCount[num] = 1
            else :
                unsortedCount[num] += 1

        #sort it
        sortedCount = sorted(unsortedCount.items(), key = lambda item : item[1], reverse = True)


        # return top k

        output = [item[0] for item in sortedCount[:k]]

        return output
