def fib():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b

n = int(input("Enter the no for printing the fibonacci series"))
for i in fib():
    if(i > n):
        break;
    print(i)  
