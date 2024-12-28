from random import randint
def guess_number():
    target_number = randint(1, 10)
    
    while True:
      try:
             user_input = int(input(f'Guess: '))
      except ValueError as e:
          print('Please enter a valid number.')
          continue
      
      if user_input > target_number:
          print(f'Guess is too high')
      elif user_input < target_number:
          print(f'Guess is too low')
      else:
          print('You guessed it right!')
          break
            


guess_number()