country = input('你是哪國人？')
age = input('你幾歲？')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你不能考')
elif country == '美國':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你不能考')
else:
	print("你只能輸入台灣跟美國")