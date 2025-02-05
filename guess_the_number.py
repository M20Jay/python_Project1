import random
EASY_LEVEL_ATTEMPTS =10
HARD_LEVEL_ATTEMPTS = 5
def set_difficulty(level_chosen):
    if level_chosen== 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS
def check_answer(guessed_number, answer):
    if guessed_number < answer:
        print("Your guess is too low")
print('let me think of a number between 1 to 50')
answer = random.randint(1,50)
print(answer)
level = input ("choose level of difficulty... type 'easy' or 'hard': ")

attempts = set_difficulty(level)
print(f'You have  {attempts} remaining to guess the number.')

guessed_number = int(input("Guess a number: "))
check_answer(guessed_number, answer)
