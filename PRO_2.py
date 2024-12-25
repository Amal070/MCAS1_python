n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
n3 = int(input("Enter the third number:"))
if(n1 > n2 and n1 > n3):
    print(f"{n1} is greater")
    n = n1
elif(n2>n3):
    print(f"{n2} is greater")
    n = n2
else:
    print(f"{n3} is greater")
    n = n3
print(n+n**2+n**3)
area = 3.14*n**2
perimeter =2*3.14*n
print(f"Area of circle = {area}")
print(f"Perimeter of circle = {perimeter}")
volume = (4/3)*3.14*n**3
print(f"Volume of sphere = {volume}")

