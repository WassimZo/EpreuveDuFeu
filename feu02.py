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
      x, y = coordinates
      if row+x < len(board) and column+y < len(board[0]) and board[row+x][column+y] != toFind[x][y] :
         return False  
   return True         

def compareMatrix(board, toFind, form) :
   boardWidth = len(board[0])
   boardHeight = len(board)
   toFindWidth = len(toFind[0])
   toFindHeigth = len(toFind)
   forms = []

   if toFindWidth > boardWidth or toFindHeigth > boardHeight :
      return "Introuvable"
   
   for row in range(len(board)) :
      for column in range(len(board[0])) :
         if formExist(row, column, board, toFind, form) : 
            forms.append([row, column])
   if forms :
      selectedForm = getTopRightForm(forms)
      formRow, formCol = selectedForm
      buildResultMatrix(formRow, formCol, board, form)
      return "Trouvé ! \nCoordonnées : %i, %i" %(formCol, formRow)
   else :
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
      x, y = coordinates
      resultMatrix[row+x][column+y] = board[row+x][column+y]

def getTopRightForm(forms) :
   maxRight = forms[0][0]
   maxTop = forms[0][0] 
   for form in forms :
      x, y = form
      if x < maxRight :
         maxRight = x 
      if y > maxTop :
         maxTop = y
   return [maxRight, maxTop]

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