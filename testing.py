infile = open('book of John text.txt','r')
file_contents = infile.read()

list = []

for x in file_contents:
    list.append(x)

print(list)