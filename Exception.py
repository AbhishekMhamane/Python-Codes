
try : 
    x = int(input("enter the 1 no for division"))
    y = int(input("enter the 2 no for division"))
    result = x/y
    print(result)
except Exception as e:
    print(type(e).__name__)