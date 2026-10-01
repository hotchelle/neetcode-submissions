class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # r: 2, a: 2, c: 2, e: 1
        # save the result in a hashmap for both and compare the hashmap

        if len(s) != len(t):
            return False

        hashmapS = {}
        hashmapT = {}

        for index, string in enumerate(s):
            if string not in hashmapS:
                hashmapS.update({string: 1})
            hashmapS[string] += 1
        

        for index, string in enumerate(t):
            if string not in hashmapT:
                hashmapT.update({string: 1})
            hashmapT[string] += 1
        

        return hashmapS == hashmapT