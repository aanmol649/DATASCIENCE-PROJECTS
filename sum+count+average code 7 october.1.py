# write a programme which repeatedly reads number until the users enters "done". once done is entered print out total ,count and average of the numbers. if the users enters anything other than a number, detect their mistakes using try and except and print an error message and skip to the next number .
number = 0 
total = 0.0
while True :
    stringvalue = input('Enter a number: ')
    if stringvalue == 'done' :
        break
    try:
        floatingvalue = float(stringvalue)
    except:
        print('invalid input')      
        continue
        print(floatingvalue)
    number = number + 1
    total = total + floatingvalue

 #print('ALL DONE')
print(total,number,total/number)
