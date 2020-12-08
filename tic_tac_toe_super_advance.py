import random
#7 8 9
#4 5 6
#1 2 3


board={7:' ',8:' ',9:' ',
        6:' ',5:' ',4:' ',
        3:' ',2:' ',1:' '}

def isMoveLeft(board):
    for i in range(1,10):
        if board[i]==' ':
            return True
    return False
def evaluate(board):
    #for rows
    for i in range(1,4):
        if board[i]==board[i+3]==board[i+6]=='o':
            return +10
        elif board[i]==board[i+3]==board[i+6]=='x':
            return -10
    # for cloumns
    for i in range(1,8,3):
        if board[i]==board[i+1]==board[i+2]=='o':
            return +10
        elif board[i]==board[i+1]==board[i+2]=='x':
            return -10
    # for diagonals
    if board[1]==board[5]==board[9]=='o':
            return +10
    elif board[1]==board[5]==board[9]=='x':
        return -10
    if board[7]==board[5]==board[3]=='o':
            return +10
    elif board[7]==board[5]==board[3]=='x':
        return -10
    else:
        return 0
def minmax(board,depth,isMax):
    score=evaluate(board)
    if score==10:
        return score
    if score==-10:
        return score
    if isMoveLeft(board)==False:
        return 0
    if isMax:
        best=-1000
        for i in range(1,10):
            if board[i]==' ':
                board[i]='o'
                best=max(best,minmax(board,depth+1,not isMax))
                board[i]=' '
        return best
    else:
        best=1000
        for i in range(1,10):
            if board[i]==' ':
                board[i]='x'
                best=min(best,minmax(board,depth+1,not isMax))
                board[i]=' '
        return best

def findBestMove(board):
    bestvalue=-1000
    bestmove=-1
    for i in range(1,10):
        if board[i]==' ':
            board[i]='o'
            moveVal=minmax(board,0,False)
            board[i]=' '
            if moveVal>bestvalue:
                bestmove=i
                bestvalue=moveVal
    print(bestmove)
    return bestmove

def printBoard(board):
    i=9
    while i !=0:
        print(board[i-2]+'|'+board[i-1]+'|'+board[i])
        print("-+-+-")
        i-=3
    i=0

def winner(board):
    for i in range(1,4):
        if board[i]==board[i+3]==board[i+6]!=' ':
            return 1
    for i in range(1,8,3):
        if board[i]==board[i+1]==board[i+2]!=' ':
            return 1
    
    if board[1]==board[5]==board[9]!=' ':
            return 1
    if board[7]==board[5]==board[3]!=' ':
            return 1
    else:
        return 0



def game(board):
    player='x'
    count=0
    for _ in range(1,10):
        printBoard(board)
        if player=='x':
            print("Turn of player  <"+player+">"+": which place to move (1-9):")
            while(1):
                try:
                    moveTo=int(input())
                    if board[moveTo]==' ':
                        board[moveTo]=player
                        break
                    else:
                        print("Please Fill in empty place")
                        print("Turn of player  <"+player+">"+" which place to move:")
                except ValueError:
                    print('Please enter postion between 1 to 9..according to your num keyboard')
        if player=='o':
            print("Turn of player  <"+player+">"+": which place to move (1-9):")
            while(1):
                try:
                    moveTo=findBestMove(board)
                    if board[moveTo]==' ':
                        board[moveTo]=player
                        break
                    else:
                        print("Please Fill in empty place")
                        print("Turn of player  <"+player+">"+" which place to move:")
                except ValueError:
                    print('Please enter postion between 1 to 9..according to your num keyboard')
        count+=1
        
        if count>=5:
            printBoard(board)
            if winner(board)==1:
                print("++ Game Over ++")
                print("Won Player"+" "+player)
                return 
        if count==9:
            print("++ Game Over ++")
            print("It's a tie game")
            return
        if player=="x":
            player='o'
        else:
            player='x'
    

if __name__ == "__main__":
    while(1):
        isPlay=input('Do you want to start the game: Enter "y" for YES and "n" for NO:')
        if isPlay in ['y',"Y"]:
            for i in board.keys():
                board[i]=' '
            game(board)
        elif isPlay in ['n',"N"]:
            print("Thanks For Playing :")
            break
        else:
            print('Enter "y" for YES and "n" for NO:')
            


        
        
        


