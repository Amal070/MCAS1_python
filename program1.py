day = int(input("Enter a day:"))
month = int(input("Enter a month:"))
year = int(input("Enter a year:"))
print(f"{day}--{month}--{year}")
if(year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
    print(f"{year} is a leap year ")
else:
    print(f"{year} is not a leap year")
