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
   print("5.Quit calculator.py\n")
   print "=" * 21
   choice = raw_input("enter choice(0/1/2/3/4):")
   return str(choice) if choice != '' else '0'
   

loop = 1

while loop == 1:
   choice = menu()

   if choice == '0':
      myhelp()
   elif choice == '5':
         loop = 0
   else:
      num1 = int(input("Enter first number: "))
      num2 = int(input("Enter second number: "))

      if choice == '1':
         print('The sum of {0} and {1} is {2}'.format(num1, num2, add(num1,num2)))
      elif choice == '2':
         print('The subtract of {0} and {1} is {2}'.format(num1, num2, subtract(num1,num2)))
      elif choice == '3':
         print('The multiply of {0} and {1} is int: {2:d} hex: {2:x}'.format(num1, num2, multiply(num1,num2)))
      elif choice == '4':
         print('The divide of {0} and {1} is {2:+08.2f}'.format(num1, num2, divide(num1,num2)))
      
      else:
         myhelp()


print "Thankyou for using calculator.py!"
