file = input("enter the file: ")
handle = open(file)
dict = dict()
for lines in handle :
    #print(lines)
    lines = lines.rstrip()
    words = lines.split()
    print(words)
    for w in words :
        if w in dict :
            dict[w] = dict[w] + 1
            print("** existing word** ")
        else:
            dict[w] = 1
            print("** new word** ")
        print(dict[w])

lis = list()
for key,value in dict.items():
    print(key,value)
    newtuple = value,key
    lis.append(newtuple)
    newtuple = sorted(lis)
print(newtuple[:])


    
