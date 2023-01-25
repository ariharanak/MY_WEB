a=int(input("ENTER"))
b=a*a
X=0
while b>0:
	rem=b%10
	X+=rem
	b//=10
if(a==X):
	print("neon")
else:
	print("not neon")
