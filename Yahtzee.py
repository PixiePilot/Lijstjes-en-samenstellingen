from random import random, randint
import collections


#import cv2
#Global functions!!!!!!!!!!!!!!!!!!!!!
totalamount = 0
 #The dices

#-------------------------------------------------------
def start():
    print('Welcome to Yahtzee')
    print('The rules are explained below here.')
    print('You get 5 dices, you will get 3 chances to throw each turn.')


def roll():
    global rolllist
    rolllist = [randint(0,6) for x in range(5)]
    # It rolls the amount of dies that has been defined in the range

            

def reroll():
    print(rolllist)

    a = 1
    while a <= 3:
        x = (int(input('Please enter the number of the dice you want to reroll: '))) 
        a = a+1
        
        if x == 1:
            dice = randint(0,6)
            del rolllist[0]
            rolllist.insert(0,(dice))
            print(rolllist)
        elif x == 2:
            dice2 = randint(0,6)
            del rolllist[1]
            rolllist.insert(1,(dice2))
            print(rolllist)
        elif x == 3:
            dice3 = randint(0,6)
            del rolllist[2]
            rolllist.insert(2,(dice3))
            print(rolllist)
        elif x == 4:
            dice4 = randint(0,6)
            del rolllist[3]
            rolllist.insert(3,(dice4))
            print(rolllist)       
        elif x == 5:
            dice5 = randint(0,6)
            del rolllist[4]
            rolllist.insert(4,(dice5))
            print(rolllist)
    rolllist.sort()
  

def checkforscore():
    print(rolllist)
    global checkscores
    checkscores = [
      list(rolllist[0:3]),
      list(rolllist[1:4]),
      list(rolllist[2:5]),
      list(rolllist),
      list(rolllist[0:4]),
      list(rolllist[1:5])
    ]
    print(checkscores)
    a = -1
    for x in range(6):
        a = a+1
        matcher(checkscores[a])


def matcher(match):
    global matcherlist,matcherlist2,before
    matcherlist = []
    matcherlist2 = []
    before = 0
#this function will look for matches for certain conditions

    match match:
        case [1,1,1]:
            for _ in rolllist:
                if _ == 1:
                    matcherlist.append(_)
                else:
                    matcherlist2.append(_)
                print(matcherlist,matcherlist2)
                before = 1

        case [2,2,2]:
            for _ in rolllist:
                if _ == 2:
                    matcherlist.append(_)
                else:
                    matcherlist2.append(_)
                print(matcherlist,matcherlist2)
                before = 1 
        case [3,3,3]:
            for _ in rolllist:
                if _ == 3:
                    matcherlist.append(_)
                else:
                    matcherlist2.append(_)
                print(matcherlist,matcherlist2)
                before = 1 
        case [4,4,4]:
            for _ in rolllist:
                if _ == 4:
                    matcherlist.append(_)
                else:
                    matcherlist2.append(_)
                print(matcherlist,matcherlist2)
                before =1 
        case [5,5,5]:
            for _ in rolllist:
                if _ == 5:
                    matcherlist.append(_)
                else:
                    matcherlist2.append(_)
                print(matcherlist,matcherlist2)
                before = 1
        case [6,6,6]:
            for _ in rolllist:
                if _ == 6:
                    matcherlist.append(_)
                else:
                    matcherlist2.append(_)
                print(matcherlist,matcherlist2)
                before = 1
        case [1,1,1,1]:
            print(7)


            
def scoreboardreset():
    global board
    board = cv2.imread('C:/Newfolder/Scoreboard.png')
    cv2.imshow('Yahtzee', board )
    cv2.waitKey(0)
    font = cv2.FONT_HERSHEY_PLAIN
    cv2.imwrite('C:/Newfolder/Scoreboard.png' + 'number1.jpg', board)
#This function is used to reset the board



def scoreboardsetlocation(x,y:int): 
                board = cv2.imread('C:/Newfolder/Scoreboard.pngnumber1.jpg')
                font = cv2.FONT_HERSHEY_PLAIN
                cv2.putText(board, (str(rollamount)), (x,y), font, 3, (0, 255, 0), 2, cv2.LINE_AA)
                cv2.imwrite('C:/Newfolder/Scoreboard.png' + 'number1.jpg', board)
                board = cv2.imread('C:/Newfolder/Scoreboard.pngnumber1.jpg')
                cv2.imshow('Yahtzee', board )
                cv2.waitKey(0)
# this is the function used place text on the screen, It has 2 input values the X pos and the Y pos


##scoreboardreset()
##roll()
##scoreboardsetlocation(220,210)
##roll()
##scoreboardsetlocation(220,237)
##roll()
##scoreboardsetlocation(220,264)
##roll()
##scoreboardsetlocation(220,291)
##roll()
##scoreboardsetlocation(220,318)
##roll()
##scoreboardsetlocation(220,345)
##if totalamount > 63:
##   totalamount = totalamount + 63

##print(totalamount)
roll()
reroll()
checkforscore()




