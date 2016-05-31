t=int(input())
if t<=10:
	temp=t
	file=open('faadu.txt','w')
	while t!=0:
		n,k=input().split(' ')
		#numbers=number.split(' ')
		#for num in numbers:
		file.write(n)
		file.write('\n')
		file.write(k)
		file.write("\n")
		t=t-1
	file.close()
	infile=open('faadu.txt','r')
	flag=0
	print("\n")
	while temp!=0:
		n=int(infile.readline())
		m=int(infile.readline())
		if m-n<100000 and 1<=n<=100000000 and 1<=m<=100000000:
			for i in range(n,m+1):
				for j in range(2,i):
					if i%j==0:
						flag=1
				if(flag==0):
	   				print(i)
				flag=0
			print("")
		temp=temp-1


				
		
			
				
				
								
	
    	
