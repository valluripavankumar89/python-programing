with open('Binary.bin','wb') as fp:
	fp.write(b'\x0456')
	fp.close()
with open('Binary.bin','ab') as fp:
	fp.write(b'\x048')
	fp.close()
with open('Binary.bin','rb') as fp:
	print(fp.read())
	fp.close()
