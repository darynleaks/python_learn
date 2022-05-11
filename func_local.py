x = 50
def func(x):
    print('x equal', x)
    x = 2
    print('switch from local x on', x)
func(x)
print ('x still', x)