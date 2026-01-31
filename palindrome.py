def is_palindrome(s):
	s=s.replace(" ","").lower()
	return s==s[::-1]
string=input("enter  astring;")
if is_palindrome(string):
	print("palindrome")
else:
	print("not palindrome")
