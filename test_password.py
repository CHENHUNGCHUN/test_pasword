count = 0
while count < 3 :
	pasword = input('請輸入密碼: ')
	if pasword == 'a123456':
		print('登入成功')
		break
	else:
		count += 1
		try_times = 3 - count
		if try_times > 0:
			print('密碼錯誤 還有{}次機會'.format(try_times))
		else:
			print('還是錯 ，帳號封鎖')	