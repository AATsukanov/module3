a = 3
b = 33

def printer(*, v, w=0.0):
    global a, b
    a = 'str'
    b = 'str-2'
    c = 6.022
    d = 1.38
    print('a, b:', a, b)
    print('c, d:', c, d)
    print('v, w:', v, w)

print('from global I: a, b', a, b)
printer(v = 'variable')
print('from global II: a, b', a, b)
