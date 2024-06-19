""" Multiple if and nested if
example of a multiple if statement: see project 2:total score/ grade"""

#nested if
name = str(input("whats your name:"))
print(f"Hello {name}, Welcome to this adventure game, good luck!!")

question = input("there is a green and red door. which one do you enter: red or green").lower()
if question == "green":
    print("great choice, on to the next level.")
    question = input("you see a river, do you swim or take the bridge").lower()
    if question == "bridge":
        print("smart move! on to the next round")
        question = input("you have seen food, would you like to eat it? yes or no").lower()
        if question == "no":
            print("good! onto the next round")
            question = input("which path do you take left or right?").lower()
            if question == "right":
                print("well done, next round")
                question = input("you have found the trasure box, do you open or close it?").lower()
                if question == "open":
                    print("yayyy!! you win the game")
                else:
                    print("sorry! you missed the treasue box")
            else:
                print("try again next time")
        else:
            print("YOU LOST!")
    else:
        print("You got eaten up by a crocodile")
else:
    print("sorry you lost!")
