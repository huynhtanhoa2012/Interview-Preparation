def marsExploration(s):
    count = 0
    for i in range(len(s)):

        if i%3 == 1:
            if s[i] != "O":
                count += 1
        else:
            if s[i] != "S":
                count += 1

    print(count)
    return count
            
marsExploration("PPSSOSSOSSOS")

# Optimal solution
def marsExploration(s):
    sos = 'SOS'
    n = len(s)
    count = 0
    for i in range(n):
        if not s[i] == sos[i%3]:
            count += 1
    return count
