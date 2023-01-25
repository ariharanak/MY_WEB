a=int(input("ENTER"))
X=0
temp=a
i=1
while i<=a//2:
	if a%i==0:
		X+=i
	i+=1
	
if(temp==X):
	print(temp,"is perfect")
else:
	print(temp,"is not perfect")
