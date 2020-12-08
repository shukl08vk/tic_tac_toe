board={7:' ',8:' ',9:' ',
        6:' ',5:' ',4:' ',
        3:' ',2:' ',1:' '}

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
            


        
        
        


