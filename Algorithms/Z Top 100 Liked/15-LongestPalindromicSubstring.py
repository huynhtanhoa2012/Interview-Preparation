def longestPalindrome(s: str) -> str:
    # The idea is to expand the pointers to left and right
    res = ""
    resLen = 0

    for i in range(len(s)):
        # odd length
        l, r = i, i
        # l and r need to be in bound, 
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l:r+1]
                resLend = r - l + 1
            # Shift left and right
            l -= 1
            r += 1

        # even length
        l, r = i, i+1
        # l and r need to be in bound, 
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l:r+1]
                resLend = r - l + 1
            # Shift left and right
            l -= 1
            r += 1
    
    return res



longestPalindrome("babad")