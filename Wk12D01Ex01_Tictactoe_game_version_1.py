import random
random.seed()   #Prepare random number generator

box1 = ""
box2 = ""
box3 = ""
over = False
winner = ""
start = int(random.random() * 2) + 1
choice = 0
count = 0
if start == 1:
    currplayer = "O"
    print("You Start " + currplayer)
else:
    currplayer = "X"
    print("You Start " + currplayer)
while over == False and count < 3:
    print(box1 + " | " + box2 + " | " + box3)
    if currplayer == "O":
        move = False
        while move == False:
            print("Enter box number (1, 2 ,3)")
            box = int(input())
            if box == 1 and box1 == "":
                box1 = "O"
                move = True
            else:
                if box == 2 and box2 == "":
                    box2 = "O"
                    move = True
                else:
                    if box == 3 and box3 == "":
                        box3 = "O"
                        move = True
                    else:
                        print("Invalid choice or Box taken")
    else:
        move = False
        while move == False:
            box = int(random.random() * 3) + 1
            if box == 1 and box1 == "":
                box1 = "X"
                move = True
            else:
                if box == 2 and box2 == "":
                    box2 = "X"
                    move = True
                else:
                    if box == 3 and box3 == "":
                        box3 = "X"
                        move = True
        print("Computer's choice " + str(box))
    choice = choice + 1
    if box1 == box2 and box2 == box3 and box1 != " ":
        print("BOARD: " + box1 + " | " + box2 + " | " + box3)
        print("GAME OVER! Computer wins!")
        over = True
    else:
        if count == 3:
            print("FINAL BOARD: " + box1 + " | " + box2 + " | " + box3)
            print("GAME OVER! It is a draw!")
            over = True
        else:
            if currplayer == "O":
                currplayer = "X"
            else:
                currplayer = "O"
