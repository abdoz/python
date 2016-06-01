import math
test_cases=int(input())
i=0
k=0
allnum={}
allnumber={}
if test_cases<=10:
	temp=test_cases
	while test_cases!=0:
		number=input()
		numbers=number.split(' ')
		for num in numbers:
			allnum[i]=num
			i=i+1
			
		test_cases=test_cases-1
	flag=0
	print("\n")
	while temp!=0:
		num1=int(allnum[k])
		k=k+1
		num2=int(allnum[k])
		k=k+1
		for i in range(1,num2+1):
			allnumber[i]=True
		for s in range(2,int(math.sqrt(num2))+1):
			for j in range(s*s,num2+1,s):
				allnumber[j]=False
		
		for d in range(num1,num2+1):
			if allnumber[d]==True:
				print(d)

				
		print("")
		temp=temp-1
