a=int(input("enter a value"))
for i in range(1,a+1):
	a*=(a-i)
	i+=1
print(f"factorial of given value is{a}")
