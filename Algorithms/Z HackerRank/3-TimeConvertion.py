def timeConversion(s):
    # Write your code here
    # 12:01:00PM
    hh = s[:2]
    mm = s[3:5]
    ss = s[6:8]
    forMat = s[8:]

    if forMat == "PM":
        if hh=="12":
            pass
        else:
            temp = int(hh) + 12
            hh = str(temp)
    elif forMat == "AM":
        if hh == "12":
            hh = "00"

    result = hh+":"+mm+":"+ss

    print(result)

timeConversion("12:45:54PM")

