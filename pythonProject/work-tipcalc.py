# Tip Calc
# Author:
# 

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent

    # Note: This is one way to round a number to two decimal places
    print(f"Leave ${round(tip, 2)}")


def dollars_to_float(d: str):
    return float(d)


def percent_to_float(p):
    return float(p) / 100


main()