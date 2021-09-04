def timer (num):
	if num <= 0:
		print ("AdictivePython")
	else: 
		print (num)
		timer(num - 1)
print(timer(10))