a=int(input("ENTER"))
X=0
temp=a
while a>0:
	b=a%10
	fact=1
	while b>0:
		fact*=b
		b-=1
	X+=fact
	a//=10

if(temp==X):
	print("strong")
else:
	print("not strong")