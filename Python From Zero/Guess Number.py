import random
number_correct = random.randint(1, 10)
guess_number = 1
while guess_number < 4:
    number_input = input('please input an integer')
    if number_input == number_correct:
        print 'you\'re great'
    else:
        print 'you\'re wrong'
        print 'you\'ve left '+str(3-guess_number)+' times'
    if guess_number == 3 and number_input != number_correct:
        print 'the correct number is ' + str(number_correct)
    guess_number = guess_number + 1


