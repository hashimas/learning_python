def fibonacci(n):
    a,b = 0,1
    while a < n:
        a,b = b, a +b
        print(a,end = ' ')

def fibonacci2(n):
    a,b = 0,1
    result = []
    while a < n:
        a,b = b, a +b
        result.append(a)
    return result

#print(fibonacci(20000))
#print(fibonacci2(20000))