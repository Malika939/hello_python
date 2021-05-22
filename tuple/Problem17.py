numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
for i in range(len(numbers)):
	if numbers [i] < 0:
		numbers[i] =-1
	elif numbers [i] > 0:
		numbers [i] = +1
	print(i)