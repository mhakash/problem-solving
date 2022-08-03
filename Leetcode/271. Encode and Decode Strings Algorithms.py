class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encodedStrings = []
        for s in strs:
            encodedStrings.append(str(len(s)) + ';' + s)
        return ''.join(encodedStrings)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        decodedStrings = []
        i = 0
        while i < len(str):
            j = i
            while str[j] != ';':
                j += 1
            strSize = int(str[i : j])
            decodedStrings.append(str[j+1 : j + 1 + strSize])
            i = j + 1 + strSize
        
        return decodedStrings