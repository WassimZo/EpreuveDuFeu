import sys 

def checkArg() :
   if len(sys.argv) != 3 : 
      return False
   return True

def createPair() :
   pair = []
   try :
      for nbr in sys.argv[1:] : 
         pair.append(int(nbr))
   except ValueError :
      print("error")
      sys.exit()
   return pair

def createRectangle(pair) :
   rows = pair[1]
   columns = pair[0]
   rectangle = [[0]*columns for row in range(rows)]
   
   for row in range(rows) :
      for column in range(columns) :
         if row == 0 and (column == 0 or column == columns-1) :
      	    rectangle[row][column] = 'o'
         elif row == rows-1 and (column == 0 or column == columns-1) :
      	    rectangle[row][column] = 'o'
         elif (column == 0 or column == columns-1) and (row != 0 or row != rows-1) :
      	    rectangle[row][column] = '|'
         elif (row == 0 or row == rows -1) and (column != 0 or column != columns-1) :
            rectangle[row][column] = '-'
         else :
            rectangle[row][column] = ' '
   return rectangle

def drawRectangle(rectangle) :
   result =""
   for row in rectangle :
      for column in row :
         result = result + column
      result = result + '\n'
   print(result[:-1])

if checkArg() :
   pair = createPair()
   rectangle = createRectangle(pair)
   drawRectangle(rectangle)
else :
   print("error")
   sys.exit()