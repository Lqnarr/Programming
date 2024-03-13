# Greet the user
print("Hello =))))")

# Ask the user's name
name = input("What is your name?: ")
print(f"Nice to meet you {name}")
# Asks them 3 question and respond specifically to those question
genshin = input("Do you play GenshinImpact? (yes/no) ")
if genshin == "yes":
    print("Booooo")
elif genshin == "no":
    print("Good")

skiOrBoard = input("Do you prefer skiing or snowboarding? ")
print(f"Nice, {skiOrBoard} is a cool sport.")

macOrWin = input("Do you prefer MacOs or Windows? ")
print(f"{macOrWin} is a good choice. I use both.")

# Says goodbye using the user's name
print(f"Anyways, goodbye {name}!")
