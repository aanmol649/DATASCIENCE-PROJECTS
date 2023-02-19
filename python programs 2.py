
#wap to input 5 numbers and find out the largest from them
a = input("enter the first number : ")
b= input("enter the second number : ")
c = input("enter the third number : ")
d = input("enter the fourth number : ")
e = input("enter the fifth number : ")
if a >= b and a>=c and a >= d and a > e :
    print("the largest number is ",a )
elif b >= a and b>=c and b >= d and b > e :
    print("the largest number is ",b )
elif c >= a and c>=b and c >= d and c > e :
    print("the largest number is ",c )
elif d >= b and d>=c and d >= a and d > e :
    print("the largest number is ",d )
elif e >= e and e>=c and e >= d and e > a :
    print("the largest number is ",e)
else :
    print("all the numbers are equal to each other")
    
for i in range(40,2,-1) :
    print(i)


# wap to input your name 50 times
name = input("enter your name: ")
for i in range(1,51,1) :
    print(name)

# wap to input name and age and print name as many times as age !
name = input("enter the name: ")
age = int(input("enter the age: "))
for i in range(1,age+1,1):
    print(name,i)

# wap to print the sum of first n natural numbers using for loop !
sum = 0
number = int(input("enter the number: "))
for i in range(1,number + 1 , 1):
    sum = sum + i
    print(sum)

#wap to print the sum of fisrt 20 even numbers()
sum = 0
for i in range(2,21,2):
    sum = sum + i
    print(sum)

# wap to input any number and print it table !
number = input("enter the value: ")
for i in range(1,11,1):
    table = float(number) * float(i)
    print((i), "*" ,(number),"=",table)

    
# wap to input 10 natural numbers using while loop !
number = 1
sum = 0
while True :
    if number <= 9 :
        number =  number + 1
        sum = number + sum
        print(number,sum)


# wap to input 10 even numbers using while loop !
number = 0
sum = 0
while True :
    if number < 20 :
        number =  number + 2
        sum = number + sum
        print(number,sum)


# wap to input 10 odd numbers using while loop !
number = 0
sum = 0
while True :
    if number < 30 :
        number =  number + 3
        sum = number + sum
        print(number,sum)

#wap to input your name and print your name 50 times using while loop !
name = (input("enter your name: "))
n = 1
while True :
    if (n < 50) :
        n = n + 1
        print(name,n)

# wap to input any 3 digit number and find out the sum of those number for ex.- input(123) = 1+ 2+ 3 = 6 !
number = int(input("enter any 3 digit number: "))
sum = 0
while number > 0 :
    b = number % 10
    sum = sum + b
    number = number // 10
    print(sum)
        
# write a programme to input any numberr and print all the factors of that number !
value = int(input("enter the value for factors: "))
for i in range(1,value+1,1):
    b = value % i 
    if b== 0 :
        print("factors are ",i)

# wap to input any number and check wheather the entered number is perfect or not !
value = int(input("enter the value for factors: "))
su = 0
for i in range(1,value,1) :
    b = value % i
    
    if b == 0 :
        print("the factors of ",value,"is",i)
        su = su + i
if (su ==value) :
    print("perfect number")
else:
   print("imperfect number")


    
    




 



        

    

            

    

    
    