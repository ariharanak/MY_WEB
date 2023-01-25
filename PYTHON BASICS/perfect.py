a=int(input("ENTER"))
Y=0
i=1
while i<=a/2:
	if a%i==0:
		Y+=i
		a//=10
	i+=1
print(i,"is perfect number of",a)
	
