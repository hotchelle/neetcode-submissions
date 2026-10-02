class Solution:

    # plan is count the length of str in strs 
    # add a delimiter after the count
    # when decoding get the count of length till you reach delim
    # then get the entire length and append to a list and return that
    # 5#Hello5#World

    def encode(self, strs: List[str]) -> str:
        res = ""

        for string in strs:
            res += str(len(string)) + "#" + string
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while (i < len(s)):
            j = i
            while (s[j] != "#"):
                j += 1
            length = int(s[i : j])
            res.append(s[j + 1 : length + j + 1])
            i = length + j + 1
        
        return res
