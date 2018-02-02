def rule188(a,b,c):
	if a == b != c:
		return '0'
	elif a == b == c == '1':
		return '0'
	return '1'

def rule110(a,b,c):
	if a== b== c:
		return '0'
	elif a== '1' and b== c == '0':
		return '0'
	else:
		return '1'
		
def display(row):
	white = u'\u25A1'
	black = u"\u25A0"
	show = ''
	for n in row:
		if n == '1':
			show += white
		else:
			show += black
	print(show)

def run(ic = '1'*45, t = 107):
	row = ic
	for _ in range(t):
		first,last = row[0],row[-1]
		nextrow = ''
		for a,b,c in zip(row,  row[1:], row[2:]):
			nextrow += rule110(a,b,c)
		row = first + nextrow + last
		display(row)

run()
