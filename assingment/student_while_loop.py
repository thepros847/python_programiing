runn = True
while run
input_value = input("Enter student's score or type "Exit" to quit":)
score = float(input_value)
if score >= 90 and score <= 100:
	print("    student wins laptop")
elif score >= 60 and score <= 89:
	print("    student wins tablet")
elif score >= 0 and score <= 59:
	print("    student wins nothing")
elif (input_value).capitalize() == "Exit":
	    break
else:
	print("score out of range!")




