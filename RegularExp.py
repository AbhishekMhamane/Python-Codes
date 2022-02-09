#importing the regular expression
import re;
# print the line contains from word

print("print the line contains from word")
file = open('demo.txt')

for line in file:
    line = line.rstrip()
    if re.search('from',line):
        print(line)

#print the line start with from
print("print the line start with from word")
file = open('demo.txt')

for line in file:
    line = line.rstrip()
    if re.search('^from',line):
        print(line)
        
# using findall method
print("using findall method")
x = "I am a 21 years old"
y = re.findall('[0-9]+',x)
print(y)