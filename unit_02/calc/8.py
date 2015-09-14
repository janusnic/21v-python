# Program make a simple calculator that can add, subtract, multiply and divide using functions

# define functions
def add(x, y):
   """This function adds two numbers"""

   return x + y

def subtract(x, y):
   """This function subtracts two numbers"""

   return x - y

def multiply(x, y):
   """This function multiplies two numbers"""

   return x * y

def divide(x, y):
   """This function divides two numbers"""

   return x / y

def myhelp():
   print " "*3 + "=" * 59
   print """   |                                                         | 
   | Usage operation:                                        |
   |     0                        Display this usage message | 
   |     1                        Add                        |  
   |     2                        Subtract                   | 
   |     3                        Multiply                   | 
   |     4                        Divide                     |
   |                                                         | """
   print " "*3 + "=" * 59

# take input from the user
def menu():
   print("Select operation:".upper().center(24, '~'))
   print("0.help".capitalize().ljust(16, '~'))
   print("1.add".title())
   print("2.Subtract")
   print("3.Multiply")
   print("4.Divide\n")
   print "=" * 21
   
   # return input("Enter choice(0/1/2/3/4):")
   return str(input("enter choice(0/1/2/3/4):".capitalize()))
   # return unicode(input("Enter choice(0/1/2/3/4):"))

choice = '0'
choice = menu()
# choice = unicode(menu())
# choice = str(menu())

if choice == '0':
   myhelp()

else:
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: "))

   if choice == '1':
      # print(num1,"+",num2,"=", add(num1,num2))
      print('The sum of {0} and {1} is {2}'.format(num1, num2, add(num1,num2)))

   elif choice == '2':
      # print(num1,"-",num2,"=", subtract(num1,num2))
      print('The subtract of {0} and {1} is {2}'.format(num1, num2, subtract(num1,num2)))

   elif choice == '3':
      # print(num1,"*",num2,"=", multiply(num1,num2))
      print('The multiply of {0} and {1} is int: {2:d} hex: {2:x}'.format(num1, num2, multiply(num1,num2)))

   elif choice == '4':
      # print(num1,"/",num2,"=", divide(num1,num2))
      print('The divide of {0} and {1} is {2:+08.2f}'.format(num1, num2, divide(num1,num2)))

   else:
      myhelp()
