def kangaroo(x1, v1, x2, v2):
    while x1<=20000 and x2<= 20000:
        if x1 == x2:
            print("YES")
            return "YES"
        x1 += v1
        x2 += v2
    
    print("NO")
    return "NO"

kangaroo(4523, 8092, 9419, 8076)