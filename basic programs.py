
# write a programme to input any character and check wheather the entered character is
# vowel :  or
# consonant !

words = input("enter the word: ")
if words == ('a' or 'A'):
    print("vowel: ",words)
elif words == ('e' or 'E'):
    print("vowel: ",words)
elif words == ('i' or 'I'):
    print("vowel: ",words)
elif words == ('o' or 'O'):
    print("vowel: ",words)
elif words == ('u' or 'U'):
    print("vowel: ",words)
 
else :
    print("consonant")

# write a programme to input two numbers and an operator ('+' ,'-','*','%','/')
first_number = float(input("enter the First number: "))
operator =  input("enter the operator('+' ,'-','*','%','/'): ")
second_number = float(input("enter the second number: "))
if operator == ('+'):
    sum = (first_number + second_number)
    print("the sum of 2 numbers is: ",sum)
elif operator == ('-'):
    substraction = (first_number - second_number)
    print("the substraction of 2 numbers is: ",substraction)
elif operator == ('*'):
    sum = (first_number * second_number)
    print("the multiplication of 2 numbers is: ",sum)
elif operator == ('/'):
    sum = (first_number / second_number)
    print("the divide of 2 numbers is: ",sum)
elif operator == ('%'):
    sum = (first_number % second_number)
    print("the divisor of 2 numbers is: ",sum)

else:
    print("invalid operator")

# write a programme in python to calculate discount offered by retailer as per the goods purchased !
#goods worth                          


#upto rupees 5000                               5%
#from  rupees 5000 to 10,000                    10%
#from rupees 10,000 to 20,000                   15%
#rupees 20,000 and above                        20%


goods = float(input("entere the cost of the goods: "))
if goods <=5000 :
    discount = (goods * 5)/100
    total = goods - discount
    print(total)
elif goods >5000 <=10000 :
    discount = (goods * 10)/100
    total = goods - discount
    print(total)
elif goods >10000 <=20000 :
    discount = (goods * 15)/100
    total = goods - discount
    print(total)
elif goods <20000 :
    discount = (goods * 20)/100
    total = goods - discount
    print(total)
else:
    print("invalid number")







