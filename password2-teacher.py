password = '12345'
i = 3 #Quota
while i > 0:
	i = i - 1
	pwd = input('Please enter your password')
	if pwd == password:
		print('Successful')
		break
	else:
		print('Wrong password!')
		if i > 0: 
			print('Remaining times:', i)
		else:
			print('Account locked')
			
