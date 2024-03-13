# Favorite programming language
# Author: Eric Gao

def main():
    favLan = input("What is your favorite programming language? ").lower().strip()
    print(reaction(favLan))
    followUpQues(favLan)


def reaction(input):
    if input == "python":
        return "🤓👆"
    elif input == "java":
        return "Wow you are OLD"
    else:
        return "Good for you :)"

def followUpQues(language):
    if language == "java":
        answer = input("Do you prefer using Intellij or Eclipse or other IDEs to write Java? ").lower().strip()
        if answer == "intellij":
            print("Intellij is great! I use it too =)")
        elif answer == "eclipse":
            print("Nice, I heard it's pretty good.")
        else:
            print("That's nice.")
    elif language == "python":
        answer = input("Do you prefer using Pycharm or VsCode to write code? ").lower().strip()
        if answer == "pycharm":
            print("I use it too =), it's good")
        elif answer == "vscode":
            print("Good for you, but it doesn't work for me sometimes so I quit using it lol.")
        else:
            print("Dang, I didn't know that software exists (Skill issue)")

main()