first_number = float(input("first number: "))
operator = input("enter the operator (+,*,/,-,% : ")
second_number = float(input("second number: "))

if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "*":
    print(first_number * second_number)
elif operator == "%":
    print(first_number % second_number)
elif operator == "/":
    print(first_number / second_number) 
else:
    print("invalid operator")
