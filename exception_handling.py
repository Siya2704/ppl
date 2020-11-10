
#raise exception
k = int(input("Enter no greater than zero "))
if k < 0:
  raise Exception("Number is negative")
  
try:
  a= int(input("Enter a number: "))
  b= int(input("Enter a number: "))

  print(a/b)
  print(c)
  print(a)
  file = open("ppl.txt","r")

except ZeroDivisionError:
	print("Division by zero not defined")

except NameError:
  print("Variable not defined")

except ValueError:
  print("Invalid input")

except FileNotFoundError:
  print("File does not exist")
  
except Exception as e:
	print(e)

else:
  print("Everything is fine")

finally:  
  print("Good bye!!")