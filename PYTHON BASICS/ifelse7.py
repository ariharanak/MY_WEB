#WPTCW the given character is alphhabet or number or special character
a=input("ENTER A CHARACTER")
if len(a)==1:
	if a>="A" and a<="Z" or a>="a" and a<="z":
		print(a,"is a alphabet")
	elif a>="0" and a<="9":
		print(a,"is a number")
	else:
		print(a,"is a special character")
else:
	print("INVALID LENGTH")