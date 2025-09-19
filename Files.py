# to use a write a text
with open('file.txt','w') as fp:
	fp.write("hello world")
	print("done")
	fp.close()
# to print a text
with open('file.txt','r') as fp:
	print(fp.read())
	fp.close()
# to append a new text in the next line
with open('file.txt','a') as fp:
	fp.write("hi pavan")
	fp.close()
with open('file.txt','r') as fp:
	print(fp.read())
	fp.close()
#to append or write multiple lines
with open('file.txt','a') as fp:
	fp.writelines(["vit","cse"])
	fp.close()
with open('file.txt','r') as fp:
	print(fp.read())
	fp.close()
#to print first line only
with open('file.txt','r') as fp:
	print(fp.readline())
	fp.close()
# to print  like a list
with open('file.txt','r') as fp:
	print(fp.readlines())
	fp.close()
#tell() are used to positon there tell
with open('file.txt','r') as fp:
	print(fp.read())
	print(fp.tell())
	fp.close()
# seek() are used to  move cusror position
with open('file.txt','r') as fp:
	print(fp.read())
	print(fp.tell())
	fp.seek(3)
	print(fp.tell())
	fp.close()
