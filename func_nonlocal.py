def func_outer():
    x = 2
    print('x equal', x)

    def func_inner():
        nonlocal x #try to replace nonlocal on 'global' and see differences
        x = 5
    func_inner()
    print('local x changed on', x)
func_outer()