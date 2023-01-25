#WPTCW the given character is Special character or not

a=input("ENTER ANY CHARACTER")

if len(a)==1:
	if a>="A" and a<="Z" or a>="a" and a<="z" or a>="0" and a<="9":
		print(a,"is not a special character")
	else:
		print(a,"is a special character")
else:
	print("INVALID LENGTH")	