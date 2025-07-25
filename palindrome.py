a=int(input("emter a vlue"))
rev=0
temp=a
while a!=0:
	digit=a%10
	rev=(rev*10)+digit
	a=a//10
if temp==rev:
	print(f"{temp} is palindrome number")
else :
	print(f"{temp} is not a pailndrome")
