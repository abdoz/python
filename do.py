import math
print("palindrome number using python ")
print("enter the number")
num=int(raw_input())
num1=len(str(num))
num1=num1-1
cons=num
i=0;
while num>0:
	temp1 = num%10
	#print(temp1)
	i=i + temp1*(10**num1)
	#print(i)
	num1=num1-1
	num=int(num/10)

if cons==i:
	print("palindrome")
else:
	print("not palindrome")




