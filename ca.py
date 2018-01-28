def rule188(a,b,c):
	if a == b != c:
		return '0'
	elif a == b == c == '1':
		return '0'
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

def run(ic = '1'*50, t = 80):
	row = ic
	for _ in range(t):
		first,last = row[0],row[-1]
		nextrow = ''
		for a,b,c in zip(row,  row[1:], row[2:]):
			nextrow += rule188(a,b,c)
		row = first + nextrow + last
		display(row)

run()