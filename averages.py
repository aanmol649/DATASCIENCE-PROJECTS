
# calculate total,number and average !
num = 0
total = 0.0
while True :
    value = input("enter the value: ")
    if value == 'done' :
        break
    try:
        fvalue = float(value)
    except:
        fvalue = ("invalid number: ")
        continue
    num = num + 1
    total = total + fvalue
print("the number,total and average is: ",num,total,total/num)

# 2nd way to calculate  average !
numlist = list()
while True :
    value = input("enter the value: ")
    if value == 'done' :
        break
    fvalue = float(value)
    numlist.append(fvalue)
    average = sum(numlist) / len(numlist)
print(average)

count = dict()
names = ['anmol','anshika','anamika','anmol','anamika']
for name in names :
    if name not in count :
        count[name] = 1
    else :
        count[name] = count[name] + 1
print(count)

count = dict()
names = ['anmol','anshika','anamika','anmol','anamika']
for name in names :
    count[name] = count.get(name,0) + 1
print(count)

count = dict()
line = input("enter the line: ")
words = line. split()
for word in words:
    count[word] = count.get(word,0) + 1 
print(count)



