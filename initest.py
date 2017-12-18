# This is a test to accept input from the user.
# Interesting Idea would be to up this to a tic tac toe cube game
# The Vairables inilitalized go here
counter = 0
Player1 = None
Player2 = None
p1 = 'X'
p2 = 'O'
bothPlayerFlag = False
gameboard = []
playerAnswer = None
Player1Answer = [0]
Player2Answer = [0]
tempValue = [0]
gameAnswers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
win = False
line6 = "9 \n"
line5 = "---|---|---\n"
line4 = " 4 |"
line3 = "3 \n"
line2 = "2 |"
line1 = " 1 |"
line7 = '6 \n'
line8 = ' 7 |'
line9 = '8 |'
line10 = '5 |'

#from Gameloop import *

#import Gameloop
#loop = Gameloop.GameStart.begin_game

# this is the function to accept user inputs and using the input to select
# the character
def userInput(x):
    global Player1
    if x == p1:
        print("Player 1 is {}".format(p1))
        Player1 = True
        return Player1
    global Player2
    if x == p2:
        print("Player 2 is {}".format(p2))
        Player2 = True
        return

# This part of the program handles user interactions within the main game loop
# specifically it directly handles the user select of the game grid and routes
# errors where they are supposed to go.
    global playerAnswer
    if playerAnswer == True:
        global Player1Answer
        global Player2Answer
        global tempValue
        '''
        try:
            tempValue = int(x)
        except ValueError():
            print("Please Enter a number between 1 and 9")
        '''
        print("Line 63: Player1Answer is {}, and Player1Answer is {}".format(Player1Answer, Player1Answer))
        tempValue = int(x)
        #gameboard.sort()
        if tempValue in gameAnswers:
            print("This is it {}".format(tempValue))
            # This loop is supposed to be testing if the value inputted is
            # valid. If not then it throws an error, if it is then it tests again
            # to check the value hasn't been entered yet.
            # if x in gameAnswers:
            # this reminder is to replace Player1Answer with specifics for Player1
            # and player2 to store each in it's own list to compair the 2 lists.
            # Currently the system is set to handle the initial value of 0 or unassigned,
            # however, it doesn't do anything with it. So This following command should be
            # used to route continued actions on the Player1 Answer.
            if Player1Answer == [0]:
                Player1Answer.append(tempValue)
                playerAnswer = False
                return Player1Answer
            if tempValue not in Player1Answer:
                if tempValue not in Player2Answer:
                    print("Number {} has been selected.".format(tempValue))
                    Player1Answer.append(tempValue)
            if tempValue in Player1Answer:
                print("Value is selected already")
                print("Line 84: tempValue = {}, and playerAnswer = {}, and Player1Answer is {}".format(tempValue, playerAnswer, Player1Answer))
                error(tempValue)
                return tempValue
            if tempValue in Player2Answer:
                print("Value is selected already")
                error(tempValue)
                return tempValue

        elif tempValue not in gameAnswers:
            #used to handle an incorrect entry, not a first time.
            print("Line 55, return error = {} is not in the list".format(Player1Answer))
            playerAnswer = False
            error(tempValue)
            return tempValue

        #if tempValue not in gameAnswers:
        # This set is copied from the player 1 and has a few differeneces
    if playerAnswer == False:
        tempValue = int(x)
        if tempValue in gameAnswers:
            # This loop is supposed to be testing if the value inputted is
            # valid. If not then it throws an error, if it is then it tests again
            # to check the value hasn't been entered yet.
            # if x in gameAnswers:
            '''
            if Player2Answer in Player1Answer:
                error(tempValue)
            if Player2Answer[0] == 0:
                print("Line 50 initial value = {} and replacing with {}".format(Player2Answer, x))
                Player2Answer = tempValue
                #print(Player1Answer)
                #print(tempValue)
                Player2Answer = False
                return Player2Answer
                '''
            if tempValue in Player1Answer:
                print("Value is selected already")
                error(tempValue)
                return tempValue
            if tempValue in Player2Answer:
                print("Value is selected already")
                error(tempValue)
                return tempValue


            # This will handle the standard user interaction rather than the
            # First time interactions
            if tempValue not in Player1Answer:
                if tempValue not in Player2Answer:
                    print("Number {} has been selected.".format(tempValue))
                    Player2Answer.append(tempValue)

            elif tempValue not in gameAnswers:
                print("Line 55, return error = {} is not in the list".format(Player2Answer))
                error(int(x))
                return Player2Answer

        if tempValue not in gameAnswers:
            print ("Line 52, return value = {}".format(Player1Answer))
            error(tempValue)

    else:
        if bothPlayerFlag == False:
            bothplayerflag = False
            error(bothPlayerFlag)

# Used very specifically to catch one error though it can expand to catch all
# Errors in the future.
def error(x):
    global bothPlayerFlag
    global tempValue
    global Player1Answer
    global Player2Answer
    if bothPlayerFlag == False:
        while bothPlayerFlag == False:
            print("X, or O only."), userInput(input().capitalize())
            bothPlayerFlag = True
            print("Line 80 tempValue is set to {}".format(tempValue))
            break


    if playerAnswer == True:
        print("line 93 tempValue current value {} ".format(tempValue))
        while tempValue not in gameAnswers:
            print("Selected value is not a valid selection. Please select a number",
            " between 1 and 9 that is not in use.")
            print("The passed in value is {}.".format(tempValue))
            if playerAnswer == True:
                tempValue = Player1Answer
            elif playerAnswer == False:
                tempValue = Player2Answer
            print("line 133, current value of gameAnswers is {}.".format(gameAnswers))
            userInput(input())
            break
        while tempValue in Player1Answer:
            print("That number is in use. Please select another number Player 1.")
            break
    if playerAnswer == False:
        print("line 93 tempValue current value {} ".format(tempValue))
        while tempValue not in gameAnswers:
            print("Selected value is not a valid selection. Please select a number",
            " between 1 and 9 that is not in use.")
            print("The passed in value is {}.".format(tempValue))
            if playerAnswer == True:
                tempValue = Player1Answer
            elif playerAnswer == False:
                tempValue = Player2Answer
            print("line 133, current value of gameAnswers is {}.".format(gameAnswers))
            userInput(input())
            break
    if tempValue in Player2Answer:
                print("That number is in use. Please select another number Player 2")

    else:
        pass



def Rules(flag):
    '''
        This is used to explain the users selected and the rules of the game as well
        as starting a new game
    '''
    global bothPlayerFlag
    global Player1
    global Player2
    if bothPlayerFlag == False:
        print("To get started Select Player 1, or Player 2 by Selecting X, or O.")
        userInput(input().capitalize())

        #The code below tests which user was selected from the previous code and,
        #then performs actions based on the results. There is a plan specifically
        #for Errors withint the 'try' statement, though I can't yet concieve of
        #any for this context so leaving it as it is for now.

    if Player1 == True:
        print("You've selected X's, Player 1.")
        print("\n The game board is layed out in a 3 by 3 grid using the number",
        "pad. \nOne being the lower grid, 2 being the middle lower, and so on."
        "\nSelect the number, in that corrisponds to the number grid.")
        print("Player 2 has been automatically assigned as O's")
        Player2 = True
        bothPlayerFlag = True
        return
    if Player2 == True:
        print("You've selected O's, Player 2.")
        print("\n The game board is layed out in a 3 by 3 grid using the number",
        "pad. \nOne being the lower grid, 2 being the middle lower, and so on."
        "\nBecause you are player 2 Player one will go first. Select the number,"
        "\nin that corrisponds to the number grid.")
        Player1 = True
        bothPlayerFlag = True
        return
    else:
        try:
            print("Something went wrong")

        except IOError as e:
            print("Something bad happened ({})".format(e))



def UI():
    '''
    This is to handle the interactions between Player 1 and Player 2. and all
    the the errors that may occur.
    '''
    global bothPlayerFlag
    global tempValue
    global gameboard
    global playerAnswer
    global Player1Answer
    if playerAnswer == True:
        print("Player one please select a number between 1 and 9.")
        userInput(input())
        playerAnswer = False
        GameStart().begin_game()
        return playerAnswer

    if playerAnswer == False:
        userInput(input("Player 2 Select a number between 1 and 9. "))
        playerAnswer = True
        GameStart().begin_game()
        return playerAnswer

'''
def gameLoop(start, stop):

    This will be used to create the game loop int it's two basic conditions.
    The Start is designed to begin the game and ensure that victory hasn't occurred.
    the stop handles victory, and Tie situations.

    pass
'''



'''
this is a test of the game loop pulled from the other file
'''

quit = 'Q'
activeGame = True
victory = False
#Player1Answer = inputtest.Player1Answer
#Player2Answer = inputtest.Player2Answer
#gameboard = inputtest.gameboard
#gameAnswers = inputtest.gameAnswers
#playerAnswer = inputtest.playerAnswer
class GameStart():
    '''
    This class is the primary game loop, however, it includes all the other states
    of the game. These interact specifically with the player answer vairables
    and in this, will then test the two against the gameAnswers to see if they
    are all in use and thus end a game in either a Tie, a P1 Victory, or a P2
    Victory.
    '''
    '''
    def __init__(self, activeGame):
        self.activeGame
    def getvictory(self):
        self.
'''

    def begin_game(self):
        # This is the game loop starting with the basic start condition. \
        # It still needs to combine the player answers and I think if the int is
        # correct it should be able to concatonate the two.
        global activeGame
        global counter
        global playerAnswer
        global gameboard
        global win
        if activeGame == True:

            while activeGame == True:
                counter += 1
                game_victory()
                if counter >= 20:
                    # This creates a list and orders the gameboard
                    # It can work anytime the counter is above 10
                    gameboard = list(set(Player1Answer)|set(Player2Answer))
                    gameboard.sort()
                    if gameboard == gameAnswers:
                        game_victory()
                        # currently surperflous and may need to be removed.
                if win == True:
                    pass
                print("line 52, counter is at {}.".format(counter))
                if victory == True:
                    print ("Congratulations!")
                    break
                elif playerAnswer == True:
                    print("Line 346: Here I am playerAnswer = {}".format(playerAnswer))
                    gameboard()
                    UI()
                elif playerAnswer == False:
                    gameboard()
                    UI()


def game_victory():
    global Player1Answer
    global Player2Answer
    global gameboard
    global game_victory
    global activeGame
    global victory
    global win
    Player1Win()
    Player2Win()
    if gameboard == gameAnswers:
        activeGame = False
        victory = True
        game_victory = True
        print("No futher moves! Game ends in a tie!")


# creating a system and a group of vairables that can identify the win status
# and excute instructions
# potential idea for creating victory is a 3d array 3 X 3 for testing X and O
# Combinations.
def Player1Win():
    global Player1Answer
    global win
    global victory
    global activeGame
    global game_victory
    winning1 = [0, 1, 2, 3]
    winning2 = [0, 4, 5, 6]
    winning3 = [0, 7, 8, 9]
    winning4 = [0, 1, 4, 7]
    winning5 = [0, 2, 5, 8]
    winning6 = [0, 3, 6, 9]
    winning7 = [0, 1, 5, 9]
    winning8 = [0, 3, 5, 7]

    Player1Answer.sort()
    winning = winning1, winning2, winning3, winning4, winning5, winning6,
    winning7, winning8

    if Player1Answer in winning1:
        print("Player 1 wins! Three across the bottom!")
        victory = True
        activeGame = False
        return
    if Player1Answer in winning2:
        print("Player 1 wins! Three across the middle!")
        victory = True
        activeGame = False
        return
    if Player1Answer == winning3:
        print("Player 1 wins! Three across the top!")
        victory = True
        activeGame = False
    if Player1Answer == winning4:
        print("Player 1 wins! Three up the left!")
        victory = True
        activeGame = False
    if Player1Answer == winning5:
        print("Player 1 wins! Three up the middle!")
        victory = True
        activeGame = False
    if Player1Answer == winning6:
        print("Player 1 wins! Three up the right!")
        victory = True
        activeGame = False
    if Player1Answer == winning7:
        print("Player 1 wins! Three diagonal from left to right!")
        victory = True
        activeGame = False
    if Player1Answer == winning8:
        print("Player 1 wins! Three diagonal from right to left!")
        victory = True
        activeGame = False
    if Player1Answer == winning:
        print("Player 1 Wins!")


def Player2Win():
    global Player1Answer
    global win
    global victory
    global activeGame
    global game_victory
    winning1 = [0, 1, 2, 3]
    winning2 = [0, 4, 5, 6]
    winning3 = [0, 7, 8, 9]
    winning4 = [0, 1, 4, 7]
    winning5 = [0, 2, 5, 8]
    winning6 = [0, 3, 6, 9]
    winning7 = [0, 1, 5, 9]
    winning8 = [0, 3, 5, 7]

    Player2Answer.sort()
    winning = winning1, winning2, winning3, winning4, winning5, winning6,
    winning7, winning8

    if Player2Answer == winning1:
        print("Player 2 wins! Three across the bottom!")
        victory = True
        activeGame = False
        return
    if Player2Answer == winning2:
        print("Player 2 wins! Three across the middle!")
        victory = True
        activeGame = False
        return
    if Player2Answer == winning3:
        print("Player 2 wins! Three across the top!")
        victory = True
        activeGame = False
    if Player2Answer == winning4:
        print("Player 2 wins! Three up the left!")
        victory = True
        activeGame = False
    if Player2Answer == winning5:
        print("Player 2 wins! Three up the middle!")
        victory = True
        activeGame = False
    if Player2Answer == winning6:
        print("Player 2 wins! Three up the right!")
        victory = True
        activeGame = False
    if Player2Answer == winning7:
        print("Player 2 wins! Three diagonal from left to right!")
        victory = True
        activeGame = False
    if Player2Answer == winning8:
        print("Player 2 wins! Three diagonal from right to left!")
        victory = True
        activeGame = False
    if Player2Answer in winning:
        print("Player 2 Wins!")


    #if win == true:
    #    pass

#def Player1win():
#    pass

#def Player2win():
#    pass



def gameboard():
    global line1
    global line2
    global line3
    global line4
    global line5
    global line6
    global line7
    global line8
    global line9
    global line10
    global Player1Answer
    global Player2Answer
#This area is setup to handle the player1 interactions with the gameboard
    for board in Player1Answer:
        if board == 1:
            line1 = ' X |'
        if board == 2:
            if gameboard in Player1Answer:
                print(Player1Answer)
            line2 = 'X |'
        if board == 3:
            line3 = 'X '
        if board == 4:
            line4 = ' X |'
        if board == 5:
            line10 = 'X |'
        if board == 6:
            line7 = 'X \n'
        if board == 7:
            line8 = ' X |'
        if board == 8:
            line9 = 'X |'
        if board == 9:
            line6 = 'X \n'
    #Player 2 responses go here.
    for board in Player2Answer:
        if board == 1:
            line1 = ' O |'
        if board == 2:
            if gameboard in Player1Answer:
                print(Player1Answer)
            line2 = 'O |'
        if board == 3:
            line3 = 'O '
        if board == 4:
            line4 = ' O |'
        if board == 5:
            line10 = 'O |'
        if board == 6:
            line7 = 'O \n'
        if board == 7:
            line8 = ' O |'
        if board == 8:
            line9 = 'O |'
        if board == 9:
            line6 = 'O \n'

    print('', line8, line9, line6, line5, line4, line10, line7, line5, line1, line2, line3)




def main():
    global playerAnswer
    global playerturn
    Rules(bothPlayerFlag)
    playerAnswer = True
    playerturn = True
    UI()








if __name__ == '__main__': main()
