a=int(input("enter"))
Y=0
Z=1
temp=a
while a>0:
	c=a%10
	Y+=c
	Z*=c
	a//=10




if Y==Z:
	print("spy number")
else:
	print("not a spy number")
