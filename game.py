import random
while True:
 option = ["R", "P", "S"]
 while True:
  yourPick = input("Enter your choice: R, P or S\n")
  if yourPick in option:
     break
  else: print("Invalid choice")

 cpuPick = random.choice(option)                            
 print(f"Player {yourPick} : CPU {cpuPick}")
 if yourPick != cpuPick:
     if yourPick == "R" and cpuPick == "P" :
         print("You lost")
         print("Game Over.")
     elif yourPick == "R" and cpuPick == "S" :
         print("You won, Congratulations!!!")
         print("Game Over.")
     elif yourPick == "P" and cpuPick == "R" :
         print("You won, Congratulations!!!")
         print("Game Over.")
     elif yourPick == "P" and cpuPick == "S" :
         print("You lost")
         print("Game Over.")
     elif yourPick == "S" and cpuPick == "R" :
         print("You lost")
         print("Game Over.")
     elif yourPick == "S" and cpuPick == "P" :
         print("You won, Congratulations!!!")
         print("Game Over.")
     break
 else: print("It's a tie!")   


