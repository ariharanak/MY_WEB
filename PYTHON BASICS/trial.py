a=153
s=0
c=3
while a>0:
	rem=a%10
	p=rem**c
	s+=p
	a//=10
print(s)