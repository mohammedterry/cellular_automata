def rule30(a,b,c):
    if int(a) + int(b) + int(c) == 1:
        return '1'
    elif a != b == c == '1':
        return '1'
    return '0'

def rule54(a,b,c):
    if int(a) + int(b) + int(c) == 1:
        return '1'
    elif b != a == c == '1':
        return '1'
    return '0'
    
def rule110(a,b,c):
    if a== b== c:
        return '0'
    elif a != b == c == '1':
        return '0'
    return '1'

def rule126(a,b,c):
    if a == b == c:
        return '0'
    return '1'

def rule188(a,b,c):
    if a == b == c == '0':
        return '0'
    elif a == b != c:
        return '0'
    return '1'

def display(row):
    white = u'\u25A1'
    black = u"\u25A0"
    show = ''
    for n in row:
        if n == '1':
            show += black
        else:
            show += white
    print(show)

def run(rule = rule110, ic = '0'*30 + '1' + '0'*30, t = 30):
    row = ic
    for _ in range(t):
        display(row)
        first,last = row[0],row[-1]
        nextrow = ''
        for a,b,c in zip(row,  row[1:], row[2:]):
            nextrow += rule(a,b,c)
        row = first + nextrow + last

run(rule = rule188)
