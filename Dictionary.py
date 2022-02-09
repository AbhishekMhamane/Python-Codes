# creating dictionary
counts = dict()
names = ['a','b','c','a']

for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)

#creating dict from file words
print('Dict of file words')
file = open('demo.txt')

di = dict()

for line in file:
    line = line.rstrip()
    words = line.split()
    
    for w in words:
        if w in di:
            di[w] = di.get(w) + 1
        else:
            di[w] = 1
print(di)
            
            
        

