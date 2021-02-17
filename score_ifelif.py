score = input('Enter Score:')
try:
	scr=float(score)
except:
	print('Enter a valid number')
	quit()

if scr >=0.0 and scr <=1.0:
	if scr >= 0.9:
		print('A')
	elif scr >= 0.8:
		print('B')
	elif scr >= 0.7:
		print('C')
	elif scr >= 0.6:
		print('D')
	elif scr < 0.6:
		print('F')

else:
	print('Input out of range')
