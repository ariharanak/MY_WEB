#WPTCW the given character is NUMBER or not
a=input("ENTER A CHARACTER")
if len(a)==1:
	if a>="0" and a<="9":
		print(a,"is a number")
	else:
		print(a,"is not a number")
else:
	print("INVALID LENGTH")