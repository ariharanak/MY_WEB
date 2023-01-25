#sum of digits of the given numbers
a=int(input("ENTER ANY NUMBER"))
sum=0
while a>0:
	sum=sum+a%10
	a//=10
print(sum)
