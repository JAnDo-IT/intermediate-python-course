
import random

def main():
  dice_rolls = 2
  dice_sum = 0
  for i in range(dice_rolls):
    roll = random.randint(1,6)
    dice_sum += roll
    print()
    #print('You rolled a die')
    print(f'You rolled a {roll}')
  
  print()
  print(f'You have rolled a total of {dice_sum}')
  print()
  
if __name__== "__main__":
  main()