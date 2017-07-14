import binascii
import sys
import os
filename = "check"
ext = ".txt"
bit = "\\x"
start =0
end = os.path.getsize(filename+ext)
for i in range(start,end*2,4):
	print ("process bit number: " + str(i))
	read = open(filename+ext,'rb')
	read = read.read()
	s = read[0:i]
	e = read[i::]
	payload = s + bit + e
	write = open(filename + ext,'wb')
	write.write(payload)
	write.close()
for i in range(start,end*2+end/48*8,48):
	if i!=0:
		print ("process bit number: " + str(i))
		read = open(filename+ext,'rb')
		read = read.read()
		s = read[0:i]
		e = read[i::]
		payload =s +'"'+ "\x0d"+"\x0a"+'"' + e
		write = open(filename + ext,'wb')
		write.write(payload)
		write.close()	
read = open(filename+ext,'rb')
read = read.read()
s = read[0:0]
e = read[0::]
payload =s +'"'+ e
write = open(filename + ext,'wb')
write.write(payload)
write.close()
read = open(filename+ext,'rb')
read = read.read()
s = read[0:end]
e = read[end::]
payload =s + e+'"'
write = open(filename + ext,'wb')
write.write(payload)
write.close()		