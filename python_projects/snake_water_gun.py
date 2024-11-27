'''
1 for snake
-1 for water 
0 for gun
'''
import random
computer = random.choice([0,1,-1])
youstr = input("Enter your choice:")
youDict = { "s":1,"g":0,"w":-1}
reverseDict = { 1:"snake",0:"gun",-1:"water"}

you = youDict[youstr]
print(f"you choose{reverseDict[you]}\ncomputer choose{reverseDict[computer]}")

if(computer == you):
    print("Draw match!")
else:
  if(computer ==-1 and you ==1):
    print("you are win!")
  elif(computer ==-1 and you ==0):
    print("you lose!")
  elif(computer ==1 and you ==-1):
    print("you loose!")
  elif(computer ==1 and you ==0):
    print("you win!")
  elif(computer ==0 and you ==1):
    print("you loose!")
  elif(computer ==0 and you ==-1):
    print("you win!")
  else:
    print("wrong input!")