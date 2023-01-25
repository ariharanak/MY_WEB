#WPTCW the given number is prime or not
a=int(input("ENTER ANY NUMBER"))
i=2
temp=0
while i<=a//2:
	if a%i==0:
		temp=1
		break
	i+=1
if temp==1:
	print("NOT PRIME NUMBER")
else:
	print("PRIME NUMBER")
