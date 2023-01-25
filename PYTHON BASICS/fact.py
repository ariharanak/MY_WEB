a=int(input("enter"))
Y=0
temp=a
while a>0:
	b=a%10
	fact=1
	while b>0:
		fact*=b
		b-=1
	Y+=fact
a//=10

if temp==Y:
	print("STRONG")