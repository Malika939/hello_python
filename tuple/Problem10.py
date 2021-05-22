a = 'h8fghy4587ty348uhfyg483y349h8werhf943c'
numbers =[]
letters =[]
for i in a:
	if i.isnumeric():
		numbers.append(int(i))
	else:
		letters.append(i)
		print(numbers,'\n',letters)