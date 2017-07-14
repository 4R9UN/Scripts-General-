


file = open('dump.txt', 'r')
a= file.readlines()
for line in a:
	words = line.split()
	for i in words:
		print words[-1]
		