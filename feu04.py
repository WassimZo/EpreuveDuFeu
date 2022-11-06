import sys

def checkNbArgs() : 
   if len(sys.argv) != 2 :
      return False
   return True

def readBoard() :
   try :
      boardFile = open(sys.argv[1])
   except FileNotFoundError :
      print("Wrong file ! ")
      sys.exit()
   return boardFile

def getNbLines(boardFile) :
   lines = boardFile.readlines()
   value = ""
   for nbr in lines[0] :
      if nbr.isnumeric() :
         value +=nbr
   try :
      nbLines = int(value)
      return nbLines
   except ValueError :
      print('Invalid map')
      sys.exit()

def getBoardCharacters(boardFile) :
   lines = boardFile.readlines()
   characters = []
   for value in lines[0] :
      if not value.isnumeric()  :
         characters.append(value)
   return characters

def createBoard(boardFile) : 
   board = []
   lines = boardFile.readlines()
   for line in lines[1:] :
      boardLine = []
      for value in line :
         boardLine.append(value)
      board.append(boardLine)
   return board

def checkBoardValidity(board, characters) :
   if board != [] and board != [['\n']]:
      length = len(board[0])
      for line in board :
         if len(line) != length or line[-1] != '\n':
            return False
         for value in line :
            if value not in characters :
               return False
      return True
   else :
      return False

def testLargestSquare(board, row, column, length, characters) :
   for squareRow in range(row, row+length) :
      for squareColumn in range(column, column+length) :
         if board[squareRow][squareColumn] == characters[1] :
            return False
   return True

def getMaxLength(board, row, column) :
   boardHeigth = len(board)
   boardWidth = len(board[0])
   maxLength = min((boardWidth-column), (boardHeigth-row))
   return maxLength

def searchLargestSquares(board, characters) :
   largestSquares = []
   for row in range(0, len(board)) :
      for column in range(0, len(board[0])) :
         length = getMaxLength(board, row, column)
         while length > 0 :
            if testLargestSquare(board, row, column, length, characters) :
               largestSquares.append([row, column, length])
               break
            else :
               length -= 1
   return largestSquares

def getLargestSquare(largestSquares) :
   maxLength = 0
   largestSquare = []
   for square in largestSquares :
      if square[2] > maxLength :
         maxLength = square[2]
   for square in largestSquares :
      if square[2] == maxLength :
         largestSquare.append(square)
   return largestSquare[0]

def boardWithLargestSquare(board, largestSquare, characters) :
   x = largestSquare[0]
   y = largestSquare[1]
   length = largestSquare[2]
   for row in range(x, x+length) :
      for column in range (y, y+length) :
         board[row][column] = characters[2]
   return board

def printBoard(board) :
   result = ""
   for line in board :
      for value in line :
         result += str(value)
   print(result)

if checkNbArgs() :
   board = createBoard(readBoard())
   characters = getBoardCharacters(readBoard())
   if checkBoardValidity(board, characters) :
      largestSquares = searchLargestSquares(board, characters)
      largestSquare = getLargestSquare(largestSquares)
      board = boardWithLargestSquare(board, largestSquare, characters)
      printBoard(board)
   else :
      print('Invalid Map !')
      sys.exit()
else :
   print("error")
   sys.exit()


