import random
# != means DOES NOT EQUAL
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
           print('Guess is too low, please try again!')
        elif guess > random_number:
           print('Guess is too high, please try again!')
    print(f'Good job, you guessed right! The number was {random_number}.')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is my {guess} too high (H), too low (L), or correct(C)? ').lower()
        if feedback == 'h':
            high= guess - 1
        elif feedback == 'l':
            low == guess + 1

    print(f'Well done! You are right, the number is {guess} ! ')


computer_guess(10)







