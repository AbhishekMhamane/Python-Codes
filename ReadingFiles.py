
#printing lines present in file demo.txt
file = open('demo.txt')
for i in file:
    print(i)

#counting lines present in the file
file = open('demo.txt')
sum = 0 
for i in file:
    sum+=1
print(sum)

#read the whole file into a single string
file = open('demo.txt')
imp = file.read()
print(len(imp))
print(imp[:20])

#print the line that starts with from word 
print("line start from ")
file = open('demo.txt')
for i in file:
    if i.startswith('from'):
        print(i)

#print the line that starts with from word 
print("line start from with rstrip()")
file = open('demo.txt')
for i in file:
    i = i.rstrip()
    if i.startswith('from'):
        print(i)