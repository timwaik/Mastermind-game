"""
A module for a text-based game of Mastermind.

    Classes:
        Mastermind

    Functions:
        run_game():
"""

import random
import time
import sys


class Mastermind:
    """
    A class to represent an instance of a Mastermind game.

        Attributes:
        --------------------
        difficulty : str
            Current difficulty of the game.
        difficultyTypes: str
            Levels of difficulty available.
        code: list
            Code to be guessed by player.
        input_code : list
            Code attempted by the player.
        loop_position : list
            Helper list to determine number of right positions.
        loop_number : list
            Helper list to determine number of right numbers.
        right_number : int
            Number of correct numbers guessed (But with incorrect position) by the player this turn.
        right_position : int
            Number of absolute correct guesses (Correct number and postiion) by the player this turn.
        turns : int
            Number of turns used to guess the correct nunmbers.

        Methods
        --------------------
        introduction(self):
            Prints welcome message and details rules of the game.

        continuer(self, statement, yesResult, noResult):
            Helper function. Accepts [Yes] or [No] input from the player and returns either True or False.

        difficulty_level(self):
            Sets the difficulty level of the game.

        new_turn(self):
            Resets all attributes required for a new turn.

        initialise_code(self):
            Sets the code to be guessed by the player.

        game(self):
            Lets the player guess the code and returns the results of the guess.

        restart_game(self):
            Determine if a new game needs to be started.
    """

    def __init__(self):
        """
        Creates initial variables for a game."""
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
        """
        Prints welcome message and details rules of the game.

            Parameters:
                None
            Returns:
                None"""

        print("Welcome to the game!\n")
        time.sleep(1)

        print(
            """
            THE RULES:
            A secret code will be generated. You win if you can guess the code.
            Numbers have to be in the right order!
            If a number is in the right position, it is considered GREEN.
            If a number is correct but in the wrong place, it is considered YELLOW.
            Good Luck!
            """
        )
        time.sleep(1)

    def continuer(self, statement, yesResult, noResult):
        """
        Helper function. Accepts [Yes] or [No] input from the player and returns either True or False.

        Parameters:
            statement : str
                statement to be answered by player
            yesResult : str
                statement to be displayed if player answers [Yes]
            noResult : str
                statement to be displayes if player answers [No]"""

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

    def difficulty_level(self):
        """
        Sets the difficulty level of the game.

        Informs player of current level and other difficulty levels available.
        Takes user input to change difficulty level.

            Parameters:
                None
            Returns:
                None"""

        difficultyDisplay = list(self.difficultyTypes.keys())
        difficultyDisplay.remove(self.difficulty)
        print(
            f"""
            The current difficulty level is {self.difficulty} ({len(self.difficultyTypes[self.difficulty])} digits)\n\
            There are two other difficulty levels:
            {difficultyDisplay[0]} ({len(self.difficultyTypes[difficultyDisplay[0]])} digits) and 
            {difficultyDisplay[1]} ({len(self.difficultyTypes[difficultyDisplay[1]])} digits)"""
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
                    print(f"Difficulty is now set to {inputDifficulty.title()}!\n")
                    self.difficulty = inputDifficulty.title()
                    break

                else:
                    print("Invalid input, try again")

            self.code = self.difficultyTypes[inputDifficulty.title()]
            self.input_code = self.difficultyTypes[inputDifficulty.title()]

    def new_turn(self):
        """
        Resets all attributes required for a new turn.

        Increments turn counter by 1

            Parameters:
                None
            Returns:
                None"""

        self.right_number = 0
        self.right_position = 0
        self.loop_position = []
        self.loop_number = []
        self.turns += 1

    def initialise_code(self):
        """
        Sets the code to be guessed by the player.

        Each value is a random int ranging from 0-9.

            Parameters:
                None
            Returns:
                None"""

        print("Setting code...")
        for x in range(len(self.code)):
            self.code[x] = int(random.randint(0, 9))
        print("The code has been set")
        # print(self.code)  # For debugging purposed, delete hash to display code

    def game(self):
        """
        Lets the player guess the code and returns the results of the guess.

            Methods:
                attempt():
                    Receives input guesses from the Player.
                correct_position():
                    Determines number of absolute correct guesses (Correct number and postiion) by the player this turn.
                correct_number():
                    Determines number of correct numbers guessed (But with incorrect position) by the player this turn.
                attempt_results():
                    Prints results of the turn. Determines if the player wins the game.
            Parameters:
                None
            Returns:
                Boolean"""

        self.new_turn()

        def attempt():
            """
            Receives input guesses from the Player.

            Guess is stored in self.input_code.

            Catches incorrect values (strings, etc) and lengths. self.turns increments for every attempt.

            Parameters:
                None
            Returns:
                None"""

            while True:
                try:
                    input_string = input(
                        "Input a number to guess, or type [quit] to exit game: \n"
                    )
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

        def correct_position():
            """
            Determines number of absolute correct guesses (Correct number and postiion) by the player this turn.

            Value is stored in self.right_position.

            Parameters:
                None
            Returns:
                None"""

            # Method 1 finding right position (use either one)
            for x in range(len(self.code)):
                if self.input_code[x] == self.code[x]:
                    self.loop_position.append(x)
                    self.right_position += 1
            # Method 2 finding right position
            """for (inputnumber, codenumber) in list(zip(self.input_code, self.code)):
                if inputnumber == codenumber:
                    self.right_position += 1"""

        def correct_number():
            """
            Determines number of numbers guessed (But with incorrect position) by the player this turn

            Value is stored in self.right_number.

            Parameters:
                None
            Returns:
                None"""

            # Method for finding right number
            for x in range(len(self.code)):
                if self.input_code[x] in self.code and x not in self.loop_position:
                    indexes = [
                        index
                        for index, number in enumerate(self.code)
                        if number == self.input_code[x]
                    ]
                    for indexNumber in indexes:
                        if indexNumber not in self.loop_position:
                            if indexNumber not in self.loop_number:
                                self.loop_number.append(indexNumber)
                                self.right_number += 1
                                break

        def attempt_results():
            """
            Prints results of the turn. Determines if the player wins the game.

            Parameters:
                None
            Returns:
                Boolean"""

            print(
                f"""
                Green: {self.right_position}
                Yellow: {self.right_number}"""
            )

            if self.right_position == len(self.code):
                print(
                    f"You win, congratulations!\n\
                        Number of tries taken: {self.turns}"
                )
                self.turns = 0
                return True
            else:
                return False

        attempt()
        correct_position()
        correct_number()
        return attempt_results()

    def restart_game(self):
        """
        Determine if a new game needs to be started.

        Parameters:
                None
            Returns:
                Boolean"""

        statement = "Do you want to play again? Enter [yes] or [no]\n"
        yesResult = "Starting again!"
        noResult = "Okay, we'll miss you. Come back soon! :("
        return self.continuer(statement, yesResult, noResult)


def run_game():
    """
    Starts an instance of a Mastermind game.

    Parameters:
        None

    Returns:
        None"""

    p1 = Mastermind()
    p1.introduction()
    while True:
        p1.difficulty_level()
        p1.initialise_code()
        while True:
            if p1.game():
                break
        if not p1.restart_game():
            break
