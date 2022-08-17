def gradingStudents(grades):
    res = []
    for i in grades:
        if i < 38:
            res.append(i)
        elif i%5 == 3:
            i = i + 2
            res.append(i)
        elif i%5 == 4:
            i = i + 1
            res.append(i)
        else:
            res.append(i)
    
    return res
        

