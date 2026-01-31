Str=input("enter a string name")
vowels='aeiouAEIOU'
count=0
for ch in Str:
	if ch in vowels:
		count+=1
print("NUMBER OF VOWELS:", count)	

