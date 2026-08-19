"""
esign an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

String encode(List<String> strs) {
    // ... your code
    return encoded_string;
}

Machine 2 (receiver) has the function:

List<String> decode(String encoded_string) {
    // ... your code
    return decoded_strs;
}

So Machine 1 does:

String encoded_string = encode(strs);

and Machine 2 does:

List<String> decoded_strs = decode(encoded_string);

decoded_strs in Machine 2 should be the same as the input strs in Machine 1.

Implement the encode and decode methods.

Example 1:

Input: strs = ["Hello","World"]

Output: ["Hello","World"]
"""

class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        i = 0
        res = []
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            leng = s[i : j]
            
            i = j + 1
            j = i + int(leng)
            res.append(s[i: j])
            i = j
        return res
 
strs = ["Hello","World"]
sol = Solution()
print(f"after encoding: {sol.encode(strs)}")
print(f"after decoding: {sol.decode(sol.encode(strs))}")