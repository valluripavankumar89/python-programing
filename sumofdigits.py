a=int(input("enter a value"))
temp=0
while a!=0:
	digit=a%10
	temp+=digit
	a=a//10
print(temp)
