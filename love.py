test_cases=int(input())
i=0
k=0
allnum={}
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
		for i in range(num1,num2+1):
			for j in range(2,i):
				if i%j==0:
					flag=1
			if(flag==0):
	   			print(i)
			flag=0
		print("")
		temp=temp-1


				
		
			
				
				
								
	
    	