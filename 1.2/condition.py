#! env python3

p = 0.06

if p <= 0.05:
	print('significant')
elif p <= 0.10:
	print('marginally significant')
else:
	print('not significant')


