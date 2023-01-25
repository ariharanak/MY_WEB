#prime or not
a=int(input("ENTER ANY NUMBER"))
temp=0
i=2
while i<=a//2:
	if a%i==0:
		temp=1
		break
	i+=1
if temp==1:
	print(a,"is not a prime number")
else:
	print(a,"is a prime number")

	