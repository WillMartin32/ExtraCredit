infile = open('book of John text.txt','r')
file_contents = infile.read()


father = 0
god = 0
christ = 0
spirit = 0
life = 0
man = 0


if('father' in file_contents):
    father += 1

#for x in file_contents:
#    word = x.split(' ')
#    if word == 'Fa':
#        father += 1


print(father)


infile.close()