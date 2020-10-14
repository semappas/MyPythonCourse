# Lame function that returns a list of beats.  
# Only runs 100 times
def current_beat():
	max = 1008
	nums = ("Y","E","K","S","H","A","H","I")
	#nums = ("S","E","F","I","D","#","E","D","W","A","R","D","#")
	#nums = ("1","H","E","S","S")
	#nums = ("C","H","A","M","I")
	#nums = ("S","H","O","G","H")
	#nums = ("S","A","Y","R","A")
	i = 0
	result = []
	while len(result) < max:
		if i >= len(nums): i = 0
		result.append(nums[i])
		i += 1
	return result

print (current_beat())