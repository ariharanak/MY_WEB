#reverse order
a=int(input("ENTER ANY NUMBER"))
rev=0
while a>0:
	rev=a%10
	print(rev)
	a//=10
	
