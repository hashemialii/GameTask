import random

while True:
    rand = random.randint(1, 10)

    while True:
        try:
            max_attempts = int(input('How many attempts would you like to \
have? '))
            if max_attempts <= 0:
                print('Please enter a positive number.')
            elif max_attempts > 10:
                print("It's too easy to choose a number! Please select a \
number of attempts up to 10.")
            else:
                break
        except ValueError:
            print('Please enter a valid number.')

    attempts = 0

    while attempts < max_attempts:
        inp = input('''Could you enter an integer to guess my number?
You should choose a number between 1 and 10 (or q or quit to quit): ''')

        if inp.lower() in ['q', 'quit']:
            break

        try:
            number = int(inp)

            if number < 1 or number > 10:
                print('You must select a number between 1 and 10')
                continue

            attempts += 1

            if number == rand:
                print(f'Well done! You won!\nNumber of your choices: {attempts}')
                break
            elif number < rand:
                print(f'Your choice is fewer than the number.\n\
You have {max_attempts - attempts} attempts left.')
            elif number > rand:
                print(f'Your choice is more than the number.\n\
You have {max_attempts - attempts} attempts left.')

            if attempts == max_attempts:
                print(f"Sorry, you've reached the maximum number of attempts!\n\
My number was: {rand}!")
                break

        except ValueError:
            print("It's not a number, please enter an integer.")

    play_again = input('Do you want to play again? (Yes or No): ').lower()
    if play_again not in ['yes', 'y']:
        print("Thanks for playing! Goodbye!")
        break
