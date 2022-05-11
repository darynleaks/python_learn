number = 23
running = True

while running:
    guess = int(input('Write numbers:'))

    if guess==number:
        print('Congratz, you are right')
        running=False #its stoping while loop
    elif guess < number:
        print('wishnes number is a bit more')
    else:
        print ('wishnes number is a bit shorter')
else:
    print('Loop while is over')
print('Finish')


