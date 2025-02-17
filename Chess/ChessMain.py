# this is our main driver file
# It will be responsible for handling user input and displaying the current GameStatus object.

import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
size = WIDTH // DIMENSION
maxfps = 35
IMAGES = {}


def loadIMAGES():
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (size, size))

        # we can access an image by saying 'IMAGES['wp']' for example

# the main driver for our code. This will handle user input and updating the graphics
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()  #   a clock object to control the frame rate
    screen.fill(p.Color("white"))   # fill the screen with white color
    gs = ChessEngine.GameState()    # create a game state object
    loadIMAGES()    # load the images
    running = True  # a boolean to keep the game running
    validMoves = gs.getValidMoves() # get the valid moves
    sqSelected = ()  # no square is selected initially, keep track of the last click of the user (tuple: (row, col))
    playerClicks = []  # keep track of player clicks (two tuples: [(6, 4), (4, 4)]) 

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:    # if the user closes the window
                running = False # stop the game
            elif e.type == p.MOUSEBUTTONDOWN:   # if the user clicks the mouse
                location = p.mouse.get_pos()  # get the x, y location of the mouse
                col = location[0]//size
                row = location[1]//size
                if sqSelected == (row, col):    # the user clicked the same square twice
                    sqSelected = () # deselect
                    playerClicks = []
                else:
                    sqSelected = (row, col) # update the user's click location 
        #what if the user clicks on the same spot twice in a row?
                    playerClicks.append(sqSelected) # append for both first and second clicks
                if len(playerClicks) == 2: # after the second click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board) # create a move object from the two clicks 
                    print(move.getChessNotation()) # print the move in chess notation 
                    if move in validMoves:  # check if the move is valid
                        gs.makeMove(move) # make the move
                        moveMade = True # a move has been made
                    gs.makeMove(move) # make the move 
                    sqSelected = () #   reset the user clicks 
                    playerClicks = []  # reset the user clicks
                
            # key handlers
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:  # undo when 'z' is pressed
                    gs.undoMove()   # undo the last move
                    moveMade = True # a move has been made
                    sqSelected = () # reset the user clicks
                    playerClicks = []   # reset the user clicks
                

        drawGameState(screen, gs)   # draw the current game state
        clock.tick(maxfps)  # make the game run at 35 fps
        p.display.flip()    # update the display

    #print(gs.board)
    p.quit()


def drawGameState(screen, gs):  # draw the squares and the pieces on the board
    drawBoard(screen)   #   draw the squares on the board
    drawPieces(screen, gs.board)    # draw the pieces on the board


# draw the squares on the board
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]    # colors of the board
    for r in range(DIMENSION):  # r is the row
        for c in range(DIMENSION):  # c is the column
            color = colors[((r+c) % 2)] # this will alternate the colors of the squares
            p.draw.rect(screen, color, p.Rect(c*size, r*size, size, size))  # draw the squares

# draw the pieces on the board using the current GameState.board
def drawPieces(screen, board):  # board is a 2d list
    for r in range(DIMENSION):  
        for c in range(DIMENSION):  
            piece = board[r][c] # get the piece at the current row and column
            if piece != "--": # if the piece is not an empty square
                # print(f"Drawing piece: {piece} at {r}, {c}")
                screen.blit(IMAGES[piece], p.Rect(c*size, r*size, size, size))# draw the piece on the board

if __name__ == "__main__":
    main()