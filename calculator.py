num1=float(input("Enter first number: "))
operator=input("Enter operator (+ , - , * , / , % ):")
num2=float(input("Enter second number: "))
if operator == '+':
    result=num1+num2
elif operator == '-':
    result=num1-num2
elif operator == '*':
    result=num1*num2
elif operator == '/':
    if num2 !=0:
      result=num1/num2
    else:
        print("Error! devision by zero ")
elif operator == '%':
    if num2 !=0:
      result=num1%num2
    else:
        print("Error! devision by zero ")
else:
    print("Invalid operator!")

print("Result: ",result)

