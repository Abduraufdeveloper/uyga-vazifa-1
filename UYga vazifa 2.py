def solutions(a, b, c):
	d = b**2 - 4*a*c
	if d == 0:
		return 1
	elif d < 0:
		return 0
	else:
		return 2