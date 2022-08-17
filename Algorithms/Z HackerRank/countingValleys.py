
# Solution uses a two pointer technique, 
# we check if current step leads to height 0 and previous height was -ve.  
height = 0
prev_height = 0
cnt = 0
n = input()
for i in range(len(s)):
    if (s[i] == 'U'):
        height += 1
    elif s[i] == 'D':
        height -= 1
    if height == 0 and prev_height < 0:
        cnt += 1
    prev_height = height
print(cnt)


def countingValleys(steps, path):

    # convert path to 1 and -1
    temp = [0]* len(path)
    for i in range(len(path)):
        if path[i] == 'D':
            temp[i] = -1
        else:
            temp[i] = 1

    res = 0
    count = 0
    seaLevel = True
    for i in range(len(temp)):
        count += temp[i]
        if count < 0 and seaLevel:
            res += 1
            seaLevel = False
        if count >= 0:
            seaLevel = True
    return res
    

countingValleys(12, "DDUUDDUDUUUD")