import random
import string

def randomd_passowerd_generator():
  length = int(input('enter the length of the password: '))

  print('''enter the type of password you want: 
        1. for alphabet
        2. arebic number
        3. punctiotion
        4. exit
        ''')

  character_list = ''

  while(True):
    choice = int(input('enter your choice: '))
    if(choice==1):
      character_list += string.ascii_letters
    elif(choice==2):
      character_list += string.digits
    elif(choice==3):
      character_list += string.punctuation
    elif(choice==4):
      break
    else:
      print('enter valide input please: ')


  password = []

  for x in range(length): 
    random_pass = random.choice(character_list)
    password.append(random_pass)

  print('the random password is: ' + '' .join(password))


option = input('do you want to generate a rondom passowerd /yes or no: ')
if(option=='yes'):
  randomd_passowerd_generator()
elif(option=='no'):
  quit
else:
  print('please enter the correst input: ')
  quit