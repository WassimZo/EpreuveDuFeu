import sys

def checkNbArgs() :
   if len(sys.argv) != 2 : 
      return False
   return True

def getExpression() :
   return sys.argv[1]

def removeSpaces(expression) :
   result = ""
   array = expression.split(' ')
   for element in array : 
      result = result + element
   return result

def DigitOrSpace(char) :
   if char.isdigit()or char == ' ' :
      return True
   else :
      return False

def getPriority(char) :
   if char == '+' or char == '-' :
      return 1
   elif char == '*' or char == '/' :
      return 2
   elif char == '%' :
      return 3
   else :
      return -1

def hasLeftAssociativity(char) :
   if char == '+' or char == '-' or char =='/' or char == '*' or char =='%' :
      return True
   else :
      return False


def peek(stack) :
   length = len(stack)
   return stack[length-1]


def infixToRpn(expression) :
   stack = []
   output = ""

   for index in range(0, len(expression)) :
      char = expression[index]

      if DigitOrSpace(char) :
         output = output+ str(char)
      elif char == '(':
         stack.append(char)
      elif char == ')' :
         while len(stack) > 0 and peek(stack) != '(' :
            output = output +' '+ stack.pop()

         if len(stack) > 0 :
            stack.pop()

      else :
         while len(stack) > 0 and getPriority(char) <= getPriority(peek(stack)) and hasLeftAssociativity(char) :
            output = output+' '+stack.pop()
         stack.append(char)

   while len(stack) > 0 :
      if peek(stack) == '(' :
         return "Error invalid expression"
      output = output+' '+ stack.pop()

   return output


def evaluate(rpnExpression) :
   stack = []
   expression = rpnExpression.split()

   for element in expression :
      if element not in '/*+-%' : 
         stack.append(int(element))
      else :
         right = stack.pop()
         left = stack.pop()
         if element == '+' :
            stack.append(left + right)
         elif element == '-' :
            stack.append(left - right) 
         elif element == '*' :
            stack.append(left * right)
         elif element == '/':
            stack.append(int(left/right))
         elif element == '%' :
            stack.append(int(left%right))
   return stack.pop()

if checkNbArgs() : 
   infixExpression = getExpression()
   rpnExpression = infixToRpn(infixExpression)
   result = evaluate(rpnExpression)
   print(result)
else :
   print("Error")
   sys.exit()

