#SQUARE ROOT
a=int(input("ENTER ANY NUMER"))
temp=0
i=2
while i<a//2:
	if i*i==a:
		temp=1
		break
	i+=1
if temp==1:
	print(i,"is the square root of",a)
else:
	print("NOT A PERFECT SQUARE ROOT")

