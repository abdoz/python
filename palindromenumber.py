import math
print("palindrome number using python ")
print("enter the number")
num=int(raw_input())
num1=len(str(num))
num1=num1-1
#save the number for future references
cons=num
i=0;
while num>0:
	# "%" will give remainder of the num means last digit
	temp1 = num%10
	#print(temp1)
	# now we are trying to reverse the number so last digit will have to multiplied 10 power length of (dig -1)
	i=i + temp1*(10**num1)
	#print(i)
	# keep decreasing num1 i.e length to make a reverse number for ex  123 will be 3*100+2*10+1*1 that is 321 
	num1=num1-1
	num=int(num/10)
#compare the number and reversed number if both are equal then the number is palindrome
if cons==i:
	print("palindrome")
else:
	print("not palindrome")




