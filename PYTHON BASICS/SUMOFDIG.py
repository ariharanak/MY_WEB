#WPT print the sum of the digits of the numbers
a=int(input("ENTER ANY NUMBER"))
sum=0
while a>0:
	rem=a%10
	sum+=rem
	a//=10
print(sum)