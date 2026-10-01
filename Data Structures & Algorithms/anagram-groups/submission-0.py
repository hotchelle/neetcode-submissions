class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we want to count each char in str
        # a through z and assign a number next to it for each alphabet present in str
        # we can then use this a through z count as the key and append all str with the
        # same key in a dictionary
        # then return this dictionary

        #first create a dictionary
        groupedAnagram = defaultdict(list)

        #iterate through each str in list of str to create the a through z count
        for string in strs:
            counterAthroughZ = [0] * 26 # a through z so len shough be 26

            # count the chars
            for char in string:
                #ord['a'] will get us the ascII value of a
                #subtracting it from the ord[char] will get us additional letters
                # like [a] - [a] = 0
                # [b] - [a] = 1 and etc
                counterAthroughZ[ord(char) - ord('a')] += 1

            #now create this as a key and append it to groupedAnagram
            groupedAnagram[tuple(counterAthroughZ)].append(string)

        return list(groupedAnagram.values())




     
        