import random
print('WELCOME! To tic tac toe game')
print('enter the number according to which you wanna input your move')
print('1    2    3\n4    5    6\n7    8    9')
cond=True
player='X'
win=None
gb=['-','-','-','-','-','-','-','-','-']
def board(gb):
    print(' | '+ gb[0] +' | '+ gb[1] + ' | '+ gb[2]+ ' | ')
    print(' | '+ gb[3] +' | '+ gb[4] + ' | '+ gb[5]+ ' | ')
    print(' | '+ gb[6] +' | '+ gb[7] + ' | '+ gb[8]+ ' | ')


def inputpl(gb):
    l=int(input('enter a number from 1 to 9: '))
    if l>=1 and l<=9 and gb[l-1]=='-':
        gb[l-1]=player
    else:
        print('The position has been already played or invalid input')


def checkrow(gb):
    global win
    if gb[0]==gb[1]==gb[2] and gb[0]!='-':
        win=gb[0]
        return True
    elif gb[3]==gb[4]==gb[5] and gb[3]!='-':
        win=gb[3]
        return True
    elif gb[6]==gb[7]==gb[8] and gb[6]!='-':
        win=gb[6]
        return True

def checkcol(gb):
    global win
    if gb[0]==gb[3]==gb[6] and gb[0]!='-':
        win=gb[0]
        return True
    elif gb[1]==gb[4]==gb[7] and gb[1]!='-':
        win=gb[1]
        return True
    elif gb[2]==gb[5]==gb[8] and gb[2]!='-':
        win=gb[2]
        return True

def checkdia(gb):
    global win
    if gb[0]==gb[4]==gb[8] and gb[0]!='-':
        win=gb[0]
        return True
    elif gb[2]==gb[4]==gb[6] and gb[2]!='-':
        win=gb[6]
        return True


def checktie(gb):
    global cond
    if '-' not in gb:
        print(board(gb))
        print("Game is a tie")
        cond=False

def checkWin():
    global cond
    if checkrow(gb) or checkcol(gb) or checkdia(gb):
        print(f'The winner is {win}')
        print(board(gb))
        cond=False

        
def switchPlayer():
    global player
    if player=='X':
        player='O'
    else:
        player='X'

def comp(gb):
    while player=='O':
        pos=random.randint(0,8)
        if gb[pos]=='-':
            gb[pos]='O'
            switchPlayer()
    

while cond:
    print(board(gb))
    inputpl(gb)
    switchPlayer()
    comp(gb)
    checkWin()
    checktie(gb)
    
#We will loose our chance to play if the player inputs a position which has been already occupied and the player is always x and the computer is o
          
