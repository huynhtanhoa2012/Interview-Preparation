def pageCount(n, p):

    # go from the beginning
    front = p//2
    if n % 2==0:
        back = (n-p+1)//2
    else:
        back = (n-p)//2
        
    return min(front, back)


pageCount(6, 5)