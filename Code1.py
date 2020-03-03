import math

def quadratic(a, b, c):
		a = int(a)
		b = int(b)
		c = int(c)
		if   ( (b**2 - 4 * a * c) < 0 ):
			print('没有根')
			pass
		elif ( (b**2 - 4 * a * c) == 0 ):
			print('唯一根')
			outcome = -b / 2*a
			print(outcome)
			pass
		elif ( (b**2 - 4 * a * c) > 0 ):
			outcome1 = ( -b + math.sqrt(b**2 - 4*a*c) )/2*a
			outcome2 = ( -b - math.sqrt(b**2 - 4*a*c) )/2*a
			print('根为')
			print('%.1f , %.1f' % (outcome1,outcome2))
			pass

def isnub(s):
	try:
		nb = float(s)
		return True
	except ValueError as e:
		return False

while 1:
	a = input('a\n')
	b = input('b\n')
	c = input('c\n')
	if not ( isnub(a) and isnub(b) and isnub(c) ):
		print('input digit please')
		continue
	else:
		quadratic(a, b, c)
