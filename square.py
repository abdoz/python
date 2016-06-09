#first function in python yayy..:P
import math
def square(num):
	return math.pow(num,2)
number1=int(raw_input("enter the range num1 :"))
number2=int(raw_input("enter num2 of range :"))

for i in range(number1,number2+1):
	print(i)
	num=int(raw_input("enter answer for above number or 0 for exiting :"))
	if num==0:
		print("game exited")
		break
	if num==square(i):
		if(i==number2):
			print("you won!")
		else:	
			print("correct!!! answer another one.")
	else:
		print("incorrect")
		print("correct answer is "+str(square(i)))		
	
