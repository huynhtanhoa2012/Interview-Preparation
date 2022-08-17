def caesarCipher(s, k):
    lowers = "abcdefghijklmnopqrstuvwxyz"
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    for c in s:
        if c in lowers:
            index = (lowers.index(c) + k)%26
            res += lowers[index]
        elif c in uppers:
            index = (uppers.index(c) + k)%26
            res += uppers[index]
        else: 
            res += c

    print(res)

caesarCipher("ABbbbC",2)