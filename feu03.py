import sys

def checkNbArgs() : 
   if len(sys.argv) != 2 :
      return False
   return True

def createGridFile() :
   try :
      gridFile = open(sys.argv[1], "r")
   except FileNotFoundError :
      print("Wrong File !")
      sys.exit()
   return gridFile

def createGrid(gridFile) :
   lines = gridFile.readlines()
   grid = []
   for line in lines :
      gridLine = []
      for value in line : 
         if value != '.' and value != '\n' :
            try :
               gridLine.append(int(value))
            except ValueError :
               print("Error")
               sys.exit()
         elif value == '.' :
            gridLine.append(0)
      grid.append(gridLine)
   return grid

def possibleValue(grid, row, column, value) :
   for x in range(9) :
      if grid[x][column] == value :
         return False
   for y in range(9) :
      if grid[row][y] == value :
         return False
   startRow = row - row%3
   startColumn = column - column % 3
   for x in range(3) :
      for y in range(3) :
      	if grid[x+startRow][y+startColumn] == value :
      	   return False
   return True

def solve(grid, row, column) :
   if row == 8 and column == 9 :
      return True
   if column == 9 :
      row = row +1 
      column = 0
   if grid[row][column] > 0 :
      return solve(grid, row, column+1)

   for value in range(1, 10) :
      if possibleValue(grid, row, column, value) : 
         grid[row][column] = value
         if solve(grid, row, column+1) :
            return True
      grid[row][column] = 0
   return False

def printResult(grid) : 
   result = "" 
   for line in grid :
      for value in line :
         result = result + str(value)
      result = result+'\n'
   print(result)

if checkNbArgs() :
   gridFile = createGridFile()
   grid = createGrid(gridFile)
   if solve(grid, 0, 0) : 
      printResult(grid)
   else :
      print("Insolvable")
      sys.exit()
else :
   print("Error")
   sys.exit()
