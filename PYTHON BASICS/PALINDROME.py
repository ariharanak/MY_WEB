#palindrome
a=int(input("ENTER ANY NUMBER"))
rev=0
temp=a
while a>0:
	rem=a%10
	rev=rev*10+rem
	a//=10
if rev==temp:
	print("PALINDROME")
else:
	print("NOT A PALINDROME")