#WPT count the number of digits in the number
a=int(input("ENTER ANY NUMBER"))
count=0
while a>0:
	a//=10
	count+=1
print(count)


    