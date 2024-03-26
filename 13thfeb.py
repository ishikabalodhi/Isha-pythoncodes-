#lambda function [even odd numbers in the list using lambda function]
list_num=[1,2,3,4,6,8,13,11,10]
list_even= list(filter(lambda n: n%2==0, list_num))
print(list_even)


list_num=[1,2,3,4,6,8,13,11,10]
list_odd= list(filter(lambda n: n%2!=0, list_num))
print(list_odd)

#use of map function
list_3=list(map(lambda n: n*2,list_even))
print(list_3)

'''(from funtion tool import reduce)
sum=reduce(fxn,iteration) {no need of type casting}'''
from funtiontool import reduce
sum= reduce(lambda a,b: a+b, list_3)
print(sum)


#number of even and odd numbers from the list
def count(list):
 ev=0
 odd=0
for i in list:
    if i%2==0:
     ev+=1
    else:
        odd+=1
      return ev
      return odd
list_4=[1,2,3,4,5,6,7,8,9,15,23,67]
even,odd=count(dist_num)
print(even,odd)
