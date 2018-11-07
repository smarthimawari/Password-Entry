password = input('please enter your password')
if password == '12345':
	print('successful')
else:
	x = 2
	while x <= 3:
		print('Remaining times:', 4-x) 
		password = input('please try again:') 
		if password == '12345':
			print('successful')
			break 
		x=x+1
		print('Fail')

