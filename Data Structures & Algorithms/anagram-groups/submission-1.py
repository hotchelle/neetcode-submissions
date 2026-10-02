class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # plan is 
        # have a char array that a through z
        # populate char array for each char in str in list and use that as a key
        # put the strs with the matching key in a hashmap
        # return the values of the matching key

        result = defaultdict(list)

        for string in strs:
            charArrayKey = [0] * 26

            for char in string:
                charArrayKey[ord(char) - ord('a')] += 1
            result[tuple(charArrayKey)].append(string)

        return list(result.values())




     
        