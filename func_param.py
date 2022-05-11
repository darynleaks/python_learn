def PrintMax(a, b):
    if a > b:
        print(a, 'is more than', b)
    elif a < b:
        print(b, 'is more than', a)
    elif a == b:
        print(a, 'equal', b)
    else:
        print(b, 'maximum')


PrintMax(3, 4)  # directly give parameters

x = 5
y = 8

PrintMax(x, y)  # giving variables as argument
