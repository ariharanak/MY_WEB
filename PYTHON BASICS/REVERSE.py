#WP TO PRINT THE GIVEN NUMBER IN REVERSE ORDER
a=int(input("ENTER ANY NUMBER"))
while a>0:
	rev=a%10
	print(rev)
	a//=10

