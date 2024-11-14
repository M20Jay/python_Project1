import random

# Print multiline instruction

print('Winning rules of the game Rock Paper Scissors are:\n'
      + "Rock vs Paper --> Paper wins \n"
      + "Rock vs Scissors --> Rock win\n"
      + "Paper vs Scissors --> Scissors win\n")
while True:
    print("Enter your choice: \n 1-Rock \n 2-Paper \n 3-Scissors \n")
    # Take the input from the user
    choice = int(input("Enter your choice :"))
    while choice > 3 or choice <1:
        choice=int(input('Enter a valid choice please: '))
    if choice == 1:
        choice_name ='Rock'
    elif choice == 2:
        choice_name ='Paper'
    else:
        choice_name ="Scissors"

    # Printing user choice
    print("User choice is:", choice_name)
    print("Now it is Computer's turn...")

    # Computer random choices
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice_name ='Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name ='Scissors'

    #Printing computer choice
    print("Computer choice is:", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    #determining the winner
    if choice == comp_choice:
        result = "Draw"
    elif (choice==1 and comp_choice == 2) or (comp_choice==1 and choice ==2):
        result ='Paper'
    elif(choice ==1 and comp_choice==3) or(comp_choice==1 and choice== 3):
        result = 'Rock'
    elif (choice==2 and comp_choice ==3) or (comp_choice==3 and choice==2):
        result = "Scissors"

    #Printing the result
    if result =="Draw":
        print("It is a tie!")
    elif result == choice_name:
        print("User wins")
    else:
        print("Computer wins")
    #Ask if the user wants to play again
    print("Do you want to play again? Y/N")
    ans= input().lower()
    if ans == 'n':
        break

    # After coming out of the while loop, print thanks for playing
print("Thanks for playing")