a=int(input("ENTER"))
c=0
s=0
p=0
temp=a
while a>0:
	a//=10
	c+=1
a=temp
while a>0:
	rem=a%10
	p=rem**c
	s+=p
	a=a//10

print(c)
print(s)
if temp==s:
	print("ARMSTRONG")
else:
	print("NOT ARMSTRONG")