num1=int(input("Let the user enter number here= "))
if num1>1:
 for i in range(2,num1+1):
  if num1%i==0:
    print("it is not a prime number")
else:
   print("it is a prime number")
