#SW 2nd Tic Tac Toe Pseudocode


#inport random module

#define user input and computer input variables
#define computer input list[1,2,3,4,5,6,7,8,9]
#define game board list[1,2,3,4,5,6,7,8,9]

#display This is Tic Tac Toe you are X he is O you win if you get three in a row. 

#create user input please input where ypu would like to play

#Create Loop
    #display game board(displays list values in lies of three: 1  2  3 next line 4  5  6 next line 7  8  9)
    #create user input please input where you would like to play
    #if input isn't valid or isn't in game borad list
        #display that the input was invalid
        #restart loop
    #else
        #remove player input from computer input list
        #replace coresponding value of player choice with X
        #if player won checking if any of these sets are equivelant (123, 149, 147, 258, 369,357, 456,789)
            #display that player won
            #break loop
        #else
            #have comuter choose random number from computer input list
            #replace coresponding value of computer choice with O
            #if computer won checking if any of these sets are equivelant (123, 149, 147, 258, 369,357, 456,789)
                #display that computer won
                #break loop
            #else
                #restart the loop
#display thank you for playing









