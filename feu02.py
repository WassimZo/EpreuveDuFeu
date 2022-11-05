import sys

resultMatrix = []

def checkNbArgs() : 
   if len(sys.argv) != 3 :
      return False
   return True


def getBoardFile() :
   try : 
      board = open(sys.argv[1], "r")
   except FileNotFoundError :
      print("Wrong file !")
      sys.exit()
   return board

def getToFindFile() :
   try : 
      toFind = open(sys.argv[2], "r")
   except FileNotFoundError :
      print("Wrong file !")
      sys.exit()
   return toFind

def getMatrix(file) :
   lines = file.readlines()
   matrix = []
   for line in lines :
      matrixLine = []
      for value in line :
         if value != '\n' :
            matrixLine.append(value)
      matrix.append(matrixLine)
   return matrix

def extractForm(toFind) :
   form = []
   row = 0
   for line in toFind :
      column = 0
      for value in line : 
         if value != ' ':
            form.append([row, column])
         column = column +1
      row = row+1 
   return form

def formExist(row, column,board, toFind, form) :
   for coordinates in form :
      if board[row+coordinates[0]][column+coordinates[1]] != toFind[coordinates[0]][coordinates[1]] :
         return False  
   return True         

def compareMatrix(board, toFind, form) :
   boardWidth = len(board[0])
   boardHeight = len(board)
   toFindWidth = len(toFind[0])
   toFindHeigth = len(toFind)

   if toFindWidth > boardWidth or toFindHeigth > boardHeight :
      return "Introuvable"
   
   row = 0
   for line in board :
      column = 0
      for value in line :
         if formExist(row, column, board, toFind, form) : 
            buildResultMatrix(row, column, board, form)
            return "Trouvé ! \nCoordonnées : %i, %i" %(column, row)
         else :
            board[row][column] = '-'
         column = column+1
      row = row+1
   return "Introuvable"

def buildResultMatrix(row, column, board, form) :
   global resultMatrix
   resultMatrix = []
   for line in board :
      noVal = []
      for value in line :
         noVal.append('-')
      resultMatrix.append(noVal)
   for coordinates in form :
      resultMatrix[row+coordinates[0]][column+coordinates[1]] = board[row+coordinates[0]][column+coordinates[1]]


def printResultMatrix(resultMatrix) :
   result = ""
   for line in resultMatrix :
      for value in line :
         result = result + value
      result = result + '\n'
   print(result) 


if checkNbArgs() :
   boardFile = getBoardFile()
   board = getMatrix(boardFile)
   toFindFile = getToFindFile()
   toFind = getMatrix(toFindFile)
   form = extractForm(toFind)
   result = compareMatrix(board, toFind, form)
   print(result)
   printResultMatrix(resultMatrix)
else : 
   print("Error")
   sys.exit()