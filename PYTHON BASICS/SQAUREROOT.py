#WP TO FIND THE SQUARE ROOT OF THE GIVEN NUMBER
a=int(input("ENTER ANY NUMBER"))
i=2
temp=0
while i<=a//2:
	if i*i==a:
		temp=1
		break
	i+=1
if temp==1:
	print(i,"is the sq.root of",a)
else:
	print(a,"has no proper square root")