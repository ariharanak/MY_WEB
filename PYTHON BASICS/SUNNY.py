#sunny
a=int(input("ENTER"))
i=2
b=a+1
v=0
while i<=b//2:
	if i*i==b:
		v=1
	i+=1
if v==1:
	print("sunny")
else:
	print("not sunny")