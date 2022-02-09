arr = list()

while(True):
    temp = int(input())
    if temp < 0 :
        break
    arr.append(temp)

print(arr)

sum = 0
for i in arr:
    if i >= 100:
        if sum != 0:
            print(sum)
            sum = 0      
        print(i)
    else:
        sum = sum + i
if sum!=0:
    print(sum)