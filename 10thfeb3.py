def fact(n):
    if (n==0 or n==1):
      return 1
    else:
        a=1
    for i in range(2,n+1):
            a=a*i
    print(a)
fact(7)

#print prime and even numbers
#factorial using recurssion
def factorial(n):
    if (n==0 or n==1):
      return 1
    else:
      return n*factorial(n-1)
n=int(input("enter a number"))
fact=factorial(n)
print("factorial of a number",fact)
