class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #all anagrams will have the same chars 
        #so we can create a map - where the key is the chars a:0, b:1, c: 0 etc
        # add all the str with the same char key to that map
        #return the map as list

        anagramMap = defaultdict(list)

        for string in strs:
            key = [0] * 26
            for char in string:
                key[ord(char) - ord('a')] += 1
            anagramMap[tuple(key)].append(string)
        
        return list(anagramMap.values())