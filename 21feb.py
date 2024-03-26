#write a function that takes a positive integer and returns the sum of the cube of all positive integers smaller than specified number.

def cube(n):
 sum=0
 for i in range (1,n):
  sum+=i**3
 return sum 
num= int(input("enter a number"))
sum=0
print(cube(num))

# write a function to print fibonacci series till n number.
def fibo(num):
 b=0
 c=1
 s=0
 while s<=num:
    print(s)
    s=c+b
    b=c
    c=s
num=int(input("enter the number upto which you want to print fibonnacci series"))
print(fibo(num))
