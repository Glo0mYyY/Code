
# Demo Fakultät
def factorial(n):
    if n == 0:
        return 1
    else:
        i = 1
        factorial = 1
        #return n * factorial(n-1)
        while i <= n:
            factorial = factorial * i
            i = i + 1        
        return factorial  

num = int(input("Geben Sie eine Zahl ein: ")) 
if num %2 == 0:
    result = factorial(num)
    print("Die Fakultät von", num, "ist", result)
else :
    print("Die Zahl", num, "ist ungerade")