def word(str):
 ptr=str.split()
 dict={}
 for i in ptr:
     if i in dict:
         dict[i]+=1
     else:
             dict[i]=1
            
 return dict
str1= input("enter the sentence:")
freq= word(str1)
print("frequency :",freq)
