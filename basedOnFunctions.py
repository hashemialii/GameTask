import random


class GuessingGame(object):

    def __init__(self):
        self.rand = 0
        self.max_attempts = 0
        self.attempts = 0

    def set_attempts(self):
        while True:
            try:
                self.max_attempts = int(input("""
How many attempts would you like to have?  """))
                if self.max_attempts <= 0:
                    print("""
Please enter a positive number.""")
                elif self.max_attempts >= 10:
                    print("""
It's too easy to choose a number! Please select a number of attempts up to 10.""")
                else:
                    break
            except ValueError:
                print("""
Please enter a valid number.""")

    @staticmethod
    def get_user_input():
        while True:
            inp = input("""
Could you enter an integer to guess my number?
You should choose a number between 1 and 10 (or q or quit to quit): """)

            if inp.lower() in ['q', 'quit']:
                return None

            try:
                number = int(inp)
                if 1 <= number <= 10:
                    return number
                else:
                    print("""
You must select a number between 1 and 10""")
            except ValueError:
                print("""
It's not a number, please enter an integer.""")

    def play_round(self):
        self.attempts = 0
        while self.attempts < self.max_attempts:
            number = self.get_user_input()
            if number is None:
                return False

            self.attempts += 1

            if number == self.rand:
                print('=' * 40)
                print(f'Well done! You won!\nNumber of your choices: {self.attempts}')
                return True
            elif number < self.rand:
                print('=' * 40)
                print(f'Your choice is fewer than the number.\nYou have {self.max_attempts - self.attempts} attempts left.')
            elif number > self.rand:
                print('=' * 40)
                print(f'Your choice is more than the number.\nYou have {self.max_attempts - self.attempts} attempts left.')

            if self.attempts == self.max_attempts:
                print('=' * 40)
                print(f"Sorry, you've reached the maximum number of attempts!\nMy number was: {self.rand}!")
                return True

    @staticmethod
    def play_again():
        play_again = input("""
Do you want to play again? (Yes or No): """).lower()
        return play_again in ['yes', 'y']

    def start_game(self):
        while True:
            self.rand = random.randint(1, 10)
            self.set_attempts()
            self.play_round()
            if not self.play_again():
                print("""

Thanks for playing! Goodbye!""")
                break


if __name__ == "__main__":

    game = GuessingGame()
    game.start_game()
