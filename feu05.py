import sys 
from collections import deque

def defineMouv(row, column, dstRow, dstCol) :
   rowMouv = []
   columnMouv = [] 
   if column > dstCol :
      if row > dstRow:
         rowMouv = [-1, 0, 0, 1]
         columnMouv = [0, -1, 1, 0]
      elif row < dstRow:
         rowMouv = [1, 0, 0, -1]
         columnMouv = [0, -1, 1, 0]
      else :
         rowMouv = [0, 0, 1, -1]
         columnMouv = [-1, 1, 0, 0]
   elif column < dstCol :
      if row > dstRow:
         rowMouv = [-1, 0, 0, 1]
         columnMouv = [0, 1, -1, 0]
      elif row < dstRow:
         rowMouv = [1, 0, 0, -1]
         columnMouv = [0, 1, -1, 0]
      else :
         rowMouv = [0, 0, 1, -1]
         columnMouv = [1, -1, 0, 0]
   else :
      if row > dstRow:
         rowMouv = [-1, 0, 0, 1]
         columnMouv = [0, -1, 1, 0]
      elif row < dstRow:
         rowMouv = [1, 0, 0, -1]
         columnMouv = [0, -1, 1, 0]
      else :
         rowMouv = [0]
         columnMouv = [0]
   return [rowMouv, columnMouv]

def checkNbArgs() : 
   if len(sys.argv) != 2 :
      return False
   return True

def readLabyrinth() :
   try :
      labyrinthFile = open(sys.argv[1])
   except FileNotFoundError :
      print("Wrong file ! ")
      sys.exit()
   return labyrinthFile

def getMapInformations(labyrinthFile) :
   lines = labyrinthFile.readlines()
   value = ""
   characters = []
   index = 0
   for character in lines[0] :
      if character.isnumeric() :
         value+=character
      else :
         if character == 'x' :
            try :
               labyrinthHeigth = int(value)
               value = ""
            except ValueError :
               print("error")
               sys.exit
         else : 
            try :
               labyrinthWidth = int(value)
               break
            except ValueError :
               print("error")
               sys.exit
      index = index +1
   characters = lines[0][index:]
   return [labyrinthHeigth, labyrinthWidth, characters]

def createLabyrinth(labyrinthFile) :
   lines = labyrinthFile.readlines()
   labyrinth = [[x for x in y[:-2]]for y in lines[1:]]
   return labyrinth

def getCharacterParams(charIndex, labyrinth, characters) :
   params = []
   for row in range(0, len(labyrinth)) :
      for column in range(0,len(labyrinth[0])) :
         if labyrinth[row][column] == characters[charIndex] :
            params= [row, column]
   return params

def testIfFree(row, column, labyrinth, visited, emptyChar, exitChar) : 
   return (row >= 0) and (row < len(labyrinth)) and (column>=0) and (column<len(labyrinth[0])) and (labyrinth[row][column] == emptyChar or labyrinth[row][column] == exitChar) and not visited[row][column]

def testIfExit(dstRow, dstCol, row, column) :
   return row == dstRow and column == dstCol

def shortestPath(labyrinth, entryParams, exitParams, emptyChar, exitChar) : 
   srcRow, srcCol = entryParams
   dstRow, dstCol = exitParams
   (height, width) = (len(labyrinth), len(labyrinth[0]))
   visited = [[False for x in range(width)] for y in range(height)]
   queue = deque()
   queue.append([srcRow, srcCol])
   path = []

   while queue :
      (row, column) = queue.popleft()
      mouveRow, mouveColumn = defineMouv(row, column, dstRow, dstCol)

      for mouve in range(4) :
         if testIfFree(row+mouveRow[mouve], column+mouveColumn[mouve], labyrinth, visited, emptyChar, exitChar) :
            if testIfExit(dstRow, dstCol, row+mouveRow[mouve], column+mouveColumn[mouve]) :
               return path 
            else :
               visited[row+mouveRow[mouve]][column+mouveColumn[mouve]] = True
               queue.append([row+mouveRow[mouve], column+mouveColumn[mouve]])
               path.append([row+mouveRow[mouve], column+mouveColumn[mouve]])
   return -1

def filterPath(path) :
   filtredPath = []
   filtredPath.append(path[0])
   for index in range(len(path)) :
      row, col = filtredPath[-1]
      nextRow, nextCol = path[index]
      if (abs(nextRow - row) == 1 and abs(nextCol - col) == 0) or (abs(nextRow-row) == 0 and abs(nextCol-col) == 1) :
         filtredPath.append(path[index])
   return filtredPath
      
def drawPath(labyrinth, path, roadChar) :
   for index in range(len(path)) :
      row, column = path[index]
      labyrinth[row][column] = roadChar
   return labyrinth


  
def printLabyrinth(labyrinth) :
   result = ""
   for line in labyrinth :
      for value in line :
         result += str(value)
      result += '\n'
   print(result[:-1])

if checkNbArgs() :
   labyrinth = createLabyrinth(readLabyrinth())
   mapInfo = getMapInformations(readLabyrinth())
   characters = mapInfo[2]
   filledChar = characters[0]
   emptyChar = characters[1]
   roadChar = characters[2]
   entryChar = characters[3]
   exitChar = characters[4]
   entryParams = getCharacterParams(3, labyrinth, characters)
   exitParams = getCharacterParams(4, labyrinth, characters)
   path = shortestPath(labyrinth, entryParams, exitParams, emptyChar, exitChar)
   if path == -1 :
      print("%sx%s%s" %(mapInfo[0], mapInfo[1], mapInfo[2][:-1]))
      printLabyrinth(labyrinth)
      print("Impossible d'atteindre la sortie !")
   else :
      path = filterPath(path)
      labyrinth = drawPath(labyrinth, path, roadChar)
      print("%sx%s%s" %(mapInfo[0], mapInfo[1], mapInfo[2][:-1]))
      printLabyrinth(labyrinth)
      print("=> SORTIE ATTEINTE EN %i COUPS !" %len(path))
else : 
   print("error")
   sys.exit()