def look_and_say(string):
	
	target = string[0]
	count = 0
	result = ""
	for number in string:
		if number == target:
			count += 1
		else:
			result += str(count) + target
			
			count = 1
			target = number
	result += str(count) + target
	return result
	
x = "1"

for i in range(30):
	x = look_and_say(x)
	
print len(x)