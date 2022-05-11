number = 23
guess = int (input ('write celoe chislo: '))
if guess == number:
    print ("congratz, you got it")
elif guess < number:
    print ("Number a bit longer that you thought")
else:
    print ("No, number is a bit shorter that you thought")
print ('finish')