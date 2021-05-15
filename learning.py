import random


# these are two different but very similar variants where v 1 is mine but v2 is smoother but it helps understanding more algorithms.
def guess0(x):
    low = 1
    high = x
    guess = ""
    variable = int(random.randint(low, high))
    while guess != "c" and low != high:
        if low == high:
            print(f"well done ,{low} is the right number. the computer guessed your number with your help ! ")
        else:
            guess = input(
                f"is {variable} the correct number ? answer [l] if the correct number is lower or [h] for higher or [c] for correct.").lower()
        if guess == "l":
            high = variable - 1
            variable = int(random.randint(low, high))
        elif guess == "h":
            low = variable + 1
            variable = int(random.randint(low, high))

    print(f"{variable} well done , the computer guessed your number with your help ! ")


def guess1(x):
    global variable
    low = 1
    high = x
    guess = ""
    while guess != "c" and low != high:
        variable = int(random.randint(low, high))
        if low == high:
            print(f"well done ,{low} is the right number. the computer guessed your number with your help ! ")
        else:
            guess = input(
                f"is {variable} the correct number ? answer [l] if the correct number is lower or [h] for higher or [c] for correct.").lower()
        if guess == "l":
            high = variable - 1

        elif guess == "h":
            low = variable + 1

    print(f"{variable} well done , the computer guessed your number with your help ! ")


guess0(100)
