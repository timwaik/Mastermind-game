import random
import time
import sys


class Mastermind:
    """docstring for Mastermind.
    introduction:"""

    def __init__(self):
        super(Mastermind, self).__init__()
        # Difficulty variables
        self.difficulty = "Easy"
        self.difficultyTypes = {"Easy": [0] * 4, "Medium": [0] * 5, "Hard": [0] * 6}
        # Input code and Secret code holders
        self.code = [0] * 4
        self.input_code = [0] * 4
        # Index holders for correct position/number guesses
        self.loop_position = []
        self.loop_number = []
        # Holder for total positions/numbers guessed correctly.
        self.right_number = 0
        self.right_position = 0
        # Turn counter holder
        self.turns = 0

    def introduction(self):
        print("Welcome to the game!\n")
        time.sleep(1)

        print(
            """
    THE RULES:
    A secret code will be generated. Your job is to guess the code.
    Numbers have to be in the right order!
    If a number is in the right position, it is considered GREEN.
    If a number is correct but in the wrong place, it is considered YELLOW.
    """
        )
        time.sleep(1)

    def continuer(self, statement, yesResult, noResult):
        while True:

            yesno = input(statement)

            if yesno.lower() == "yes":
                print(yesResult, "\n")
                return True
                break

            elif yesno.lower() == "no":
                print(noResult, "\n")
                return False
                break

            else:
                print("Invalid input, try again")

    def difficultyLevel(self):
        difficultyDisplay = list(self.difficultyTypes.keys())
        difficultyDisplay.remove(self.difficulty)
        print(
            f"The current difficulty level is {self.difficulty}\n\
                There are two other difficulty levels, {difficultyDisplay[0]} and {difficultyDisplay[1]}"
        )
        statement = (
            "\nWould you like to change the difficulty level? Enter [Yes] or [No]\n"
        )
        yesResult = "Changing difficulty..."
        noResult = "Difficulty stays the same\n"

        if self.continuer(statement, yesResult, noResult):
            while True:
                print("What difficulty would you like to change it to?")
                print(f"Enter {difficultyDisplay[0]} or {difficultyDisplay[1]}")
                inputDifficulty = input()

                if inputDifficulty.title() in difficultyDisplay:
                    print(f"Difficulty is now set to {inputDifficulty.lower()}!\n")
                    self.difficulty = inputDifficulty.lower()
                    break

                else:
                    print("Invalid input, try again")

            self.code = self.difficultyTypes[inputDifficulty.title()]
            self.input_code = self.difficultyTypes[inputDifficulty.title()]

    def new_turn(self):
        self.right_number = 0
        self.right_position = 0
        self.loop_position = []
        self.loop_number = []
        self.turns += 1

    def initialise_code(self):
        print("Setting code...")
        for x in range(len(self.code)):
            self.code[x] = int(random.randint(0, 9))
        print("The code has been set")
        print(self.code)  # For debugging purposed, delete hash to display code

    def game(self):
        self.new_turn()
        while True:
            try:
                input_string = input("Input a number, or type [quit] to exit game: \n")
                if input_string.lower() == "quit":
                    sys.exit("Goodbye!")
                self.input_code = list(map(int, list(input_string)))
                if len(input_string) != len(self.code):
                    print("You didn't enter the right amount of numbers, try again")
                    self.turns += 1
                else:
                    break
            except ValueError:
                print("You didn't input a number! Try again")
                self.turns += 1

        # Method 1 finding right position (use either one)
        for x in range(len(self.code)):
            if self.input_code[x] == self.code[x]:
                self.loop_position.append(x)
                self.right_position += 1

        # Method 2 finding right position
        """for (inputnumber, codenumber) in list(zip(self.input_code, self.code)):
            if inputnumber == codenumber:
                self.right_position += 1"""

        # Method for finding right number
        for x in range(len(self.code)):
            if self.input_code[x] in self.code and x not in self.loop_position:
                bla = [
                    index
                    for index, number in enumerate(self.code)
                    if number == self.input_code[x]
                ]
                for indexNumber in bla:
                    if indexNumber not in self.loop_position:
                        if indexNumber not in self.loop_number:
                            self.loop_number.append(indexNumber)
                            self.right_number += 1
                            break

        print(
            f"Green: {self.right_position}\n\
              Yellow: {self.right_number}"
        )

        if self.right_position == len(self.code):
            print(
                f"You win, congratulations!\n\
                    Number of tries taken: {self.turns}"
            )
            return True
        else:
            return False

    def end_game(self):
        self.turns = 0
        statement = "Do you want to play again? Enter [yes] or [no]\n"
        yesResult = "Starting again!"
        noResult = "Okay, we'll miss you. Come back soon! :("
        return self.continuer(statement, yesResult, noResult) == True


def main():
    p1 = Mastermind()
    p1.introduction()
    while True:
        p1.difficultyLevel()
        p1.initialise_code()
        while True:
            if p1.game() == True:
                break
        if p1.end_game() == False:
            break


main()
