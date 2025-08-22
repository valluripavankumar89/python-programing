Str=input("enter a string name")
words=Str.split()
for word in words:
	if len(word)%2==0:
		print(word)
