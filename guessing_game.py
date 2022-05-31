import random

class GuessingGame():
    def __init__(self, answer):
        self.answer = answer
        self.is_solved = False
       
    def guess_check(self):
        while self.is_solved == False:
            user_guess = int(input("enter a number: "))
            if user_guess == self.answer:
                print(f"You solved it! {user_guess} is the correct answer {self.answer}.")
                self.is_solved = True
            elif user_guess < self.answer:
                print("guess higher")
            elif user_guess > self.answer:
                print("guess lower")

def main():
    game = GuessingGame(10)
    print(game.guess_check())

if __name__ == "__main__": 
    main()



# ----- DRIVER CODE -----
#game = GuessingGame(random.randint(1,100))

