def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a
user=int(input("Enter the fibonposition you want: "))
print(fibonacci(user))
