'''
number = 23
running = False

while running:
    guess = int (input ('vvedite celoe chislo: '))
    if guess == number:
        print ('congratz')

    elif guess < number:
        print ('net, nemnogo bolshe')
    else:
        print ('net, nemnogo menwe')
'''

'''''
for i in list(range(1,5)):
    print(i)
'''''

'''''
while True:
    s = input ('vvedit chto nibud:')
    if s == 'vuxod':
        break
    if len(s) < 3:
        print ('sliwkom malo')
        continue
    print('vvedennata stroka dostatochno')
'''

while True:
   daryn = input ('tupeet if eat smth bad:')
   if daryn == 'vegatables and fruits':
      print ('smart daryn')
      break
   elif daryn == 'eat shit':
      print ('daun prekreshai')
