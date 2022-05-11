x = 50

def func ():
    global x

    print ('x equal', x)
    x = 2
    print ('Switching from global variable x on', x)

func ()
print('X is equal on', x)