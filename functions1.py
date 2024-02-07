#write a python program to create a function that does arithematic addition, subtractionand division of two numbers

def func(a,b):
  sum=a+b
  sub=b-a
  multiply= a*b
  divide= b/a
  print(sum)
  print(sub)
  print(multiply)
  print(divide)
func(19,20)  

#write a python program code to print the reverse of a function

str="stay in dreams"
new=str[::-1]
print(new)

#write a function to check if the given year is leap year
def check_leap_year(year):
    if year % 4 == 0:
        print("Leap year")
    else:
        print("Not a leap year")

user_input = int(input("Enter a year: "))
check_leap_year(user_input)
