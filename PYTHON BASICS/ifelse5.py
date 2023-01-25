#WPTCW the given character is vowels or consonants
a=input("ENTER ANY ALPHABETS")
if len(a)==1:
	if a>="A" and a<="Z" or a>="a" and a<="z":
		if a=="a" or a=="e" or a=="i" or a=="o" or a=="u" or a=="A" or a=="E" or a=="I" or a=="O" or a=="U":
			print(a,"is a vowel")
		else:
			print(a,"is a consonant")
	else:
		print("THE GIVEN CHARACTER IS NOT A ALPHABET")
else:
	print("IVALID LENGTH")