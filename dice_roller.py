import random
import time

def main():
  dice_rolls = input("How many times you want to roll the dice?\n> ")
  dice_size = input("What The Size of the dice you want?\n>")
  dice_sum = 0

  for i in range(0,int(dice_rolls)):
      if dice_rolls.isalpha() or dice_size.isalpha():
        print("Sorry That's not a number\n---------------------")
        main()
      elif dice_rolls.isdigit():
        time.sleep(1)
      else:
        print("sorry i don't understand you")
      roll = random.randint(1,6)
      dice_sum += roll
      if roll == 1:
        print(f"You rolled a {roll} Critical Failed :(")
      elif roll == 6:
        print(f"You rolled a {roll} Critical Success :)")
      else:
        print(f"You rolled a {roll}")
  print(f"You have rolled a total of {dice_sum}")


if __name__== "__main__":
  main()