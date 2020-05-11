password  = 'a123456'
i = 0
n = 2
while i < 3:
	if input('請輸入密碼: ') == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤! 還有', n, '次機會')
		n = n - 1
		i = i + 1
		if n < 0:
			break