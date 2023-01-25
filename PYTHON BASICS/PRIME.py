a=int(input("ENTER"))
i=2
temp=0
while i<=a//2:
	if a%i==0:
		temp=1
		break
	i+=1
if temp==1:
	print(a," is not an prime number")
else:
	print(a,"is  prime number")




















