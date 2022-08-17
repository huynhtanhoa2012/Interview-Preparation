def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    length = 0
    if len(password) <= 6:
        length = 6 - len(password)
    
    number = 1
    lower = 1
    upper = 1
    special = 1
    for c in password:
        if c in numbers:
            number = 0
        if c in lower_case:
            lower = 0
        if c in upper_case:
            upper = 0
        if c in special_characters:
            special = 0
    print(max((number+lower+upper+special), length))
    return max((number+lower+upper+special), length)

minimumNumber(5, "#HackerRank")
