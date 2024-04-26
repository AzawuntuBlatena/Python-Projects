def add(a,b):
  answer = a+b
  print(str(a) + "+" + str(b) + "=" + str(answer))
def sub(a,b):
  answer= a-b 
  print(str(a) + "-" + str(b) + "=" + str(answer))

def mul(a,b):
  answer= a*b
  print(str(a) + "*" + str(b) + "=" + str(answer))

def div(a,b):
  answer= a/b
  print(str(a) + "/" + str(b) + "=" + str(answer))

while True:
  print("well come to the calculator \n")
  print("A  for Addition")
  print("B  for Subtraction")
  print("C  for mltiplication")
  print("D  for division")
  print("E  for exit")
  choice = input('enter your choise please: ')

  if choice == "a" or choice == "A":
    print("Addition")
    a= int(input('enter input 1: \t'))
    b= int(input('enter input 2: \t'))
    add(a,b)
  elif choice == "b" or choice== "B":
    print("Subtraction")
    a = int(input("enter tnput 1 \t"))
    b = int(input("enter input 2 \t"))
    sub(a,b)
  elif choice == "c" or choice== "C":
    print("Multiplication")
    a = int(input("enter input 1 \t"))
    b = int(input("enter input 2 \t"))
    mul(a,b)
  elif choice == "D" or choice== "d":
    print("Division")
    a = int(input("enter input 1 \t"))
    b = int(input("enter input 2 \t"))
    div(a,b)
  elif choice == "e" or choice== "E":
   print("the programe is ended")
   quit()