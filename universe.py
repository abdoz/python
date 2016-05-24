print("input:")
i=0
arr={}
num=0
while num!=42:
	num=int(raw_input())
	arr[i]=num
	i=i+1
	
num1=len(arr)-1
j=0
print("output:")
while j<=num1:
	if(arr[j]!=42):
		print(arr[j])
		j=j+1
	else:
		break
		

