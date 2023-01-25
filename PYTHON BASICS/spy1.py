a=int(input("ENTER"))
X=0
Y=1
while a>0:
	b=a%10
	X+=b
	Y*=b
	a//=10
if X==Y:
	print("SPY NUMBER")
else:
	print("NOT SPY NUMBER")
