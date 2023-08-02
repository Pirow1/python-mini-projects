print(" Welcome To My Quiz Game \n Interesting Game to Play")
Player = input(" Do you want to play the game? \n" )
if Player.lower() != 'yes':
    print("Good Bye")
    quit()  

name_player = input("Enter Your Name: ")

print("Let's Start the Game :) ",name_player)

score = 0

answer = input(' What does CPU stand for? \n ')
if answer.lower() == 'central processing unit':
    print("Correct")
    score += 1
else:
    print('Wrong')
 
answer = input(' What does GPU stand for? \n ')
if answer.lower() == 'graphical processing unit':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' What does RAM stand for? \n ')
if answer.lower() == 'random access memory':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' What does ROM stand for? \n ')
if answer.lower() == 'read only memory':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' Is a Mouse an input device or output device? \n ')
if answer.lower() == 'input device':
    print("Correct")
    score += 1
else:
    print('Wrong')

#Extra questions
answer = input(' What does ALU stand for in the context of computers? \n ')
if answer.lower() == 'arithmetic logic unit':
    print("Correct")
    score += 1
else:
    print('Wrong')
 
answer = input(' What is Half Byte called? \n ')
if answer.lower() == 'Nibble':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' What does SSD stand for? \n ')
if answer.lower() == 'solid state drive':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' What does the collection of 8 bits make? \n ')
if answer.lower() == 'byte':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' What does GUI stand for? \n ')
if answer.lower() == 'graphical user interface':
    print("Correct")
    score += 1
else:
    print('Wrong')
    
print("You got the " + str(score)+ " correct answers")
print("You got the " + str((score/5) *100)+ " correct answers")
