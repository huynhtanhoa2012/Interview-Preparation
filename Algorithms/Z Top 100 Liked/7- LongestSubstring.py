def lengthOfLongestSubstring(s: str) -> int:

    max_length = 0
    i = 0
    j = 0
    hashset = set()

    while j < len(s):
        if s[j] not in hashset:
            hashset.add(s[j])
            j += 1
            max_length = max(max_length, j-i)
        else:
            hashset.remove(s[i])
            i += 1
        

    print(max_length)
    return max_length
            
lengthOfLongestSubstring("pwwkew")