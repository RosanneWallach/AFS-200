import random;

def randomNum () :
  return random.randint(1,9)

def guessingGame () :
  endGame = False
  num = randomNum()
  while endGame != True :
    guess = input('Guess a number between 1 and 9!')
    if guess.__contains__("Exit") :
      endGame = True
      print("Thanks For Playing!")
    elif int(guess) == num :
      print("Congrats! Let's keep playing")
    elif int(guess) > num :
      print("Too High, try again...")
    elif int(guess) < num :
      print("Too Low, try again...")

guessingGame()