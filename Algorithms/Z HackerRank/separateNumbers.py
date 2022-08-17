def separateNumbers(s):
    # s = "1234"
    d = 1
    digits = ""
    def generate(digits, length):
        

    while d < len(s):
        for i in range(d):
            digits += s[i]
            generate(digits, len(s))
    return n