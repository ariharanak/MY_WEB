#WPTCW the given alphabet is UPPERCASE or LOWERCASE
a=input("ENTER ANY ALPHABET")
if len(a)==1:
	if a>="A" and a<="Z" or a>="a" and a<="z":
		if a>="A" and a<="Z":
			print(a,"is UPPER CASE")
		else:
			print(a, "is LOWER CASE")
	else:
		print("THE GIVEN CHARACTER IS NOT ALPHABET")
else:
	print("IVALID LENGTH")