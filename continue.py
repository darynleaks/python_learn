while True:
    s = input ('Say something:')
    if s == 'exit':
        break
    if len(s) < 3:
        print ('Very short')
        continue
    print ('Typed letters is enought')
    #something else here