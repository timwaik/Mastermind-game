import random , time
import sys

class Mastermind():
    """docstring for Mastermind."""
    def __init__(self):
        super(Mastermind, self).__init__()
        #Difficulty variables
        self.difficulty = "easy"
        self.difficultyTypes = ["easy", "medium", "hard"]
        #Input code and Secret code holders
        self.code = [0] * 4
        self.input_code = [0] * 4
        #Index holders for correct position/number guesses
        self.loop_position = []
        self.loop_number = []
        #Holder for total positions/numbers guessed correctly.
        self.right_number = 0
        self.right_position = 0
        #Turn counter holder
        self.turns = 0

    def continuer(self, statement, Yesresult, noResult):
        while True:

            yesno = input(statement)

            if yesno.lower() == 'yes':
                print(Yesresult, '\n')
                return True
                break

            elif yesno.lower() == 'no':
                print(noResult, '\n')
                return False
                break

            else:
                print('Invalid input, try again')

    def new_turn(self):
        self.right_number = 0
        self.right_position = 0
        self.loop_position = []
        self.loop_number = []
        self.turns += 1

    def introduction(self):
        print("Welcome to the game!\n")
        time.sleep(2)

        print('THE RULES:')
        print("A secret code will be generated. Your job is to guess the code.")
        print("Numbers have to be in the right order!")
        print("If a number is in the right position, it is considered GREEN")
        print("If a number is correct but in the wrong place, it is considered YELLOW")
        time.sleep(2)

    def difficultyLevel(self):
        difficultyDisplay = self.difficultyTypes.copy()
        difficultyDisplay.remove(self.difficulty)
        print("The current difficulty level is '%s'" % self.difficulty)
        print("There are two other difficulty levels, '%s' and '%s'" \
        % (difficultyDisplay[0], difficultyDisplay[1]))
        statement = "\nWould you like to change the difficulty level? Enter \
 [Yes] or [No]\n"
        Yesresult = "Changing difficulty..."
        noResult = "Difficulty stays the same\n"

        if self.continuer(statement, Yesresult, noResult) == True:
            while True:
                print("What difficulty would you like to change it to?")
                print("Enter '%s' or '%s'" % (difficultyDisplay[0], difficultyDisplay[1]))
                inputDifficulty = input()

                if inputDifficulty.lower() == difficultyDisplay[0]:
                    print('Difficulty is not set to %s!\n' % difficultyDisplay[0])
                    self.difficulty = difficultyDisplay[0]
                    break

                elif inputDifficulty.lower() == difficultyDisplay[1]:
                    print('Difficulty is now set to %s!\n' % difficultyDisplay[1])
                    self.difficulty = difficultyDisplay[1]
                    break

                else:
                    print("Invalid input, try again")

            if self.difficulty == "easy":
                self.code = [0] * 4
                self.input_code = [0] * 4
            elif self.difficulty == "medium":
                self.code = [0] * 5
                self.input_code = [0] * 5
            elif self.difficulty == "hard":
                self.code = [0] * 6
                self.input_code = [0] * 6

    def initialise_code(self):
        print('Setting code...')
        for x in range(len(self.code)):
            self.code[x] = int(random.randint(0, 9))
        print('The code has been set')
        print(self.code) #For debugging purposed, delete hash to display code


    def game(self):
        self.new_turn()
        while True:
            try:
                input_string = input("Input a number, or type [quit] to exit game: \n")
                if input_string.lower() == "quit":
                    sys.exit("Goodbye!")
                self.input_code = list(input_string)
                self.input_code = list(map(int, self.input_code))
                if len(input_string) != len(self.code):
                    print("You didn't enter the right amount of numbers, try again")
                    self.turns += 1
                else:
                    break
            except ValueError:
                print("You didn't input a number! Try again")
                self.turns += 1

        #Method 1 finding right position (use either one)
        for x in range(len(self.code)):
            if self.input_code[x] == self.code[x]:
                self.loop_position.append(x)
                self.right_position += 1

        #Method 2 finding right position
        """for (inputnumber, codenumber) in list(zip(self.input_code, self.code)):
            if inputnumber == codenumber:
                self.right_position += 1"""

        #Method for finding right number
        for x in range(len(self.code)):
            if self.input_code[x] in self.code:
                if x not in self.loop_position:
                    bla = [index for index,number in enumerate(self.code) if number == self.input_code[x]]
                    for indexNumber in bla:
                        if indexNumber not in self.loop_position:
                            if indexNumber not in self.loop_number:
                                self.loop_number.append(indexNumber)
                                self.right_number += 1
                                break

        print("Green: ", self.right_position)
        print("Yellow: ", self.right_number)

        if self.right_position == len(self.code):
            print("You win, congratulations!")
            print("Number of tries taken: ", self.turns)
            return True
        else:
            return False

    def end_game(self):
        self.turns = 0
        statement = 'Do you want to play again? Enter [yes] or [no]\n'
        Yesresult = 'Starting again!'
        noResult = "Okay, we'll miss you. Come back soon! :("
        return self.continuer(statement, Yesresult, noResult) == True


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
