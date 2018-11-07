password = '12345'
entry = input('please enter your password')
if entry == password:
	print('successful')
else:
	x = 0
	while x < 2:
		print('Remaining times:', 2-x) 
		entry = input('please try again:') 
		if entry == password:
			print('successful')
			break
		x = x + 1
	print('Sorry you failed')
	


	




