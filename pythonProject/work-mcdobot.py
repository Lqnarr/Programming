# Mcdobot

answer = input("Do you want fries with your meal? ")
answerOriginal = answer
answer.strip().lower()

if answer == "yes":
    print("Here's your meal with fries.")
elif answer == "no":
    print("Okay, no fries in your meal.")
else:
    print(f"Sorry, I don't understand what {answerOriginal} is.")