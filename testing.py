from os import X_OK


infile = open('book of John text.txt','r')
file_contents = infile.read()

#list = []

#for x in file_contents:
 #   list.append(x)

#print(list)

dict = {}
y = 1


#for x in file_contents:
#    dict[y] = x
#    y += 1

if ('father' in file_contents):
    dict[y] = 'father'
    y +=1


print(dict)