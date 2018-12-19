import random

class SecretNumberGame:
    def __init__(self):
        self.randomNumber = random.randint(1,100)
    
    def generateRandomNumber(self):
        self.randomNumber = random.randint(1,100)

    def getGuess(self):
        self.guess = int(input("Your guess on the Secret Number (1-99): "))

    def getResult(self):
        if self.guess < self.randomNumber:
            print ("It is higher than..", self.guess)
        elif self.guess > self.randomNumber:
            print ("It is lower than..", self.guess)
        else:
            print ("\n","B I N G O !")
    
    def gameEnded(self):
        return self.guess != self.randomNumber

print ("Welcome to Guess-the-Secret-Number Game!","\n")

num = SecretNumberGame()
num.generateRandomNumber() # Generate random number
num.getGuess() # Get userinput guess
num.getResult() # Compares guess with the random number, get hints

while num.gameEnded(): # While guess is not correct
    num.getGuess() # continue to get user input guess
    num.getResult()
