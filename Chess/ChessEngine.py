# this class is responsible for storing all the information about the current game state.
# it will also be responsible for determining the valid moves at the current state. 
# it will also keep a move log.
# This class will also be responsible for updating the board state and will also move pieces.

# the GameState class will keep track of all the information about the current state of the game.
class GameState():
    def __init__(self) -> None:
        self.board = [  # an 8x8 2d list, each element of the list has 2 characters
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"], #
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"], # pawns
            ["--", "--", "--", "--", "--", "--", "--", "--"],  # empty spaces
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.moveFunctions = {'p': self.getPawnMoves, 
                              'R': self.getRookMoves, 
                              'N': self.getKnightMoves, 
                              'B': self.getBishopMoves, 
                              'Q': self.getQueenMoves, 
                              'K': self.getKingMoves} 
                            # dictionary to map pieces to their move functions
        self.whiteToMove = True # if it is white's turn to move
        self.moveLog = [] # log of all the moves that have been made in the game


    # takes a move as a parameter and executes it (this will not work for castling, pawn promotion, and en-passant)
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--" # empty the start square 
        self.board[move.endRow][move.endCol] = move.pieceMoved  # move the piece to the end square 
        self.moveLog.append(move)   # log the move so we can undo it later 
        self.whiteToMove = not self.whiteToMove # swap players
    
    # undo the last move made
    def undoMove(self):
        if len(self.moveLog) != 0:   # make sure there is a move to undo 
            move = self.moveLog.pop()   # get the last move from the move log 
            self.board[move.startRow][move.startCol] = move.pieceMoved  # put the piece back on the start square 
            self.board[move.endRow][move.endCol] = move.pieceCaptured  # put the captured piece back on the end square 
            self.whiteToMove = not self.whiteToMove # switch turns back

    # all moves considering checks
    def getValidMoves(self):
        return self.getAllPossibleMoves()   # for now we will not worry about checks


    # all moves without considering checks
    def getAllPossibleMoves(self):
        moves = []  # list to store all the possible moves
        for r in range(len(self.board)):    # number of rows
            for c in range(len(self.board[r])): # number of columns in a row
                turn = self.board[r][c][0]  # get the color of the piece
                print("turn")
                if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):    # if it is the player's turn to move  
                    piece = self.board[r][c][1] # get the piece type
                    self.moveFunctions[piece](r, c, moves)  # call the appropriate move function based on the piece type

                    
                    # if piece == 'p':    # pawn
                    #     self.getPawnMoves(r, c, moves)  # get all the pawn moves
                    # elif piece == 'R':  # rook
                    #     self.getRookMoves(r, c, moves)  # get all the rook moves
                    # elif piece == 'N':  # knight
                    #     self.getKnightMoves(r, c, moves)
                    # elif piece == 'B':
                    #     self.getBishopMoves(r, c, moves)
                    # elif piece == 'Q':
                    #     self.getQueenMoves(r, c, moves)
                    # elif piece == 'K':
                    #     self.getKingMoves(r, c, moves)
        return moves
    
    # get all the pawn moves for the pawn located at row, col and add these moves to the list 
    def getPawnMoves(self, r, c, moves):    # r = row, c = col, moves = list of moves
        if self.whiteToMove:    # white pawn moves
            if self.board[r-1][c] == "--":  # 1 square pawn advance
                moves.append(Move((r, c), (r-1, c), self.board))    # add the move to the list of moves
                if r == 6 and self.board[r-2][c] == "--":  # 2 square pawn advance
                    moves.append(Move((r, c), (r-2, c), self.board)) # only on the starting row 
            if c-1 >= 0:    # captures to the left
                if self.board[r-1][c-1][0] == 'b':  # enemy piece to capture
                    moves.append(Move((r, c), (r-1, c-1), self.board))  # add the move to the list of moves
            if c+1 <= 7:    # captures to the right
                if self.board[r-1][c+1][0] == 'b':  # enemy piece to capture
                    moves.append(Move((r, c), (r-1, c+1), self.board))  # add the move to the list of moves
            # understand why the rows and collumns have additions and substractions
        # once the pawns are moved first, the black pawn moves are implemented.
        # but what if the player moves the horse first?
                    
        else:   # black pawn moves
            if self.board[r+1][c] == "--":  # 1 square pawn advance
                moves.append(Move((r, c), (r+1, c), self.board))
                if r == 1 and self.board[r+2][c] == "--":
                    moves.append(Move((r, c), (r+2, c), self.board))
            if c-1 >= 0:    # captures to the left
                if self.board[r+1][c-1][0] == 'w':
                    moves.append(Move((r, c), (r+1, c-1), self.board))
            # if c+1 <= len(self.board)-1:
            # if c+1 <= len(self.board[0]):
            if c+1 <= 7:    # captures to the right
                if self.board[r+1][c+1][0] == 'w':  # enemy piece to capture
                    moves.append(Move((r, c), (r+1, c+1), self.board))  # add the move to the list of moves

    #
    def getRookMoves(self, r, c, moves):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1)) # up, left, down, right 
        enemyColor = 'b' if self.whiteToMove else 'w' # if it is white's turn, the enemy color is black 
        # if self.whiteToMove: # if it is white's turn
        #     enemyColor = 'b'    # the enemy color is black
        # else: 
        #     enemyColor = 'w'
        for d in directions:   # for each direction
            for i in range(1, 8): # for each square in that direction
                endRow = r + d[0] * i # new row
                endCol = c + d[1] * i # new col
                if 0 <= endRow < 8 and 0 <= endCol < 8: # on board

                    endPiece = self.board[endRow][endCol] # get the piece at the end square
                    if endPiece == "--": # empty square valid
                        moves.append(Move((r, c), (endRow, endCol), self.board) )   #
                    elif endPiece[0] == enemyColor: # enemy piece valid 
                        moves.append(Move((r, c), (endRow, endCol), self.board)) # capture the enemy piece
                        break # stop the loop after capturing the enemy piece
                    else:   # friendly piece invalid
                        break   # stop the loop after encountering a friendly piece
                else:   # off board
                    break


    def getKnightMoves(self, r, c, moves): # r = row, c = col, moves = list of moves
        knightMoves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)) # all possible knight moves
        allyColor = 'w' if self.whiteToMove else 'b' # if it is white's turn, the ally color is white
        for m in knightMoves:
            endRow = r + m[0]
            endCol = c + m[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8: # on board
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != allyColor: # not an ally piece
                    moves.append(Move((r, c), (endRow, endCol), self.board))
                    
    def getKingMoves(self, r, c, moves): # r = row, c = col, moves = list of moves
        directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        enemyColor = 'b' if self.whiteToMove else 'w' # if it is white's turn, the enemy color is black
        for d in directions:
            endRow = r + d[0]
            endCol = c + d[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8: # on board
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != enemyColor: # not an enemy piece
                    moves.append(Move((r, c), (endRow, endCol), self.board))
       

    def getBishopMoves(self, r, c, moves): # r = row, c = col, moves = list of moves
        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1)) # up-left, up-right, down-left, down-right
        enemyColor = 'b' if self.whiteToMove else 'w'
        for d in directions:
            for i in range(1, 8):
                endRow = r + d[0] * i
                endCol = c + d[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "--":
                        moves.append(Move((r, c), (endRow, endCol), self.board))
                    elif endPiece[0] == enemyColor:
                        moves.append(Move((r, c), (endRow, endCol), self.board))
                        break
                    else:
                        break
                else:
                    break

    def getQueenMoves(self, r, c, moves):   # r = row, c = col, moves = list of moves
        # instead of re implementing the moves, just add the rook and bishop moves
        self.getRookMoves(r, c, moves)  # queen moves like a rook
        self.getBishopMoves(r, c, moves)    # queen moves like a bishop

    def getKingMoves(self, r, c, moves): # r = row, c = col, moves = list of moves
        directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        enemyColor = 'b' if self.whiteToMove else 'w'
        for d in directions:
            endRow = r + d[0]
            endCol = c + d[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != enemyColor:
                    moves.append(Move((r, c), (endRow, endCol), self.board))
                        

class Move():
    # maps keys to values
    # key : value
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0} # 8 is the top row, 1 is the bottom row
    rowsToRanks = {v: k for k, v in ranksToRows.items()}   # 0 is the top row, 7 is the bottom row
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}  # a is the leftmost column, h is the rightmost column
    colsToFiles = {v: k for k, v in filesToCols.items()}    # 0 is the leftmost column, 7 is the rightmost column

    def __init__(self, startSq, endSq, board) -> None:  # startSq = (row, col) endSq = (row, col)   board = 2d list of strings 
        self.startRow = startSq[0] # row of the start square
        self.startCol = startSq[1] # col of the start square
        self.endRow = endSq[0] # row of the end square
        self.endCol = endSq[1] # col of the end square
        self.pieceMoved = board[self.startRow][self.startCol]   # the piece that moved from start square to end square 
        self.pieceCaptured = board[self.endRow][self.endCol]    #the piece that was captured    (can be '--' if no piece was captured) 
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol    # unique id for the move 
        print(self.moveID)

    # overwriting the equals method
    def __eq__(self, o: object) -> bool:# o is the object we are comparing to 
        if isinstance(o, Move):# check if the object is an instance of the Move class 
            return self.moveID == o.moveID# compare the moveID of the two moves 



    def getChessNotation(self): 
        return self.getRankFiles(self.startRow, self.startCol) + self.getRankFiles(self.endRow, self.endCol)  # add logic to handle pawn promotion later    
    
    def getRankFiles(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r] # helper method to get rank and file of a square in chess notation 