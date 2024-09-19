"""
Lesson 2: control flow

Play a game of 4 questions
"""

# is it round?
# is it heavy?
# do you hold it when you use it?
# is it a daily household item?

# NOTE: The key indicates the answers to the above questions,
# in order. "1" indicates a yes, "0" indicates a no.
items = {
    "1111": "frying pan",
    "1110": "bowling ball",
    "1101": "circular dining table",
    "1100": "earth",
    "1011": "Plastic cup w/o anything in it",
    "1010": "frisbee",
    "1001": "lightbulb",
    "1000": "bubble",
    "0111": "lawn mower",
    "0110": "bricks",
    "0101": "TV",
    "0100": "giraffe",
    "0011": "chopsticks",
    "0010": "pocketknife",
    "0001": "pillow",
    "0000": "square cloud", 
}


def run_four_questions():
    answer = input("Is it round? (y/n): ")
    final_key = ""
    if answer == "y":
        final_key += "1"
    elif answer == "n":
        final_key += "0"
    else:
        raise ValueError(f"Expected y/n but got {answer}")

    answer = input("Is it heavy? (y/n): ")
    if answer == "y":
        final_key += "1"
    elif answer == "n":
        final_key += "0"
    else:
        raise ValueError(f"Expected y/n but got {answer}")

    answer = input("Do you hold it when you use it? (y/n): ")
    if answer == "y":
        final_key += "1"
    elif answer == "n":
        final_key += "0"
    else:
        raise ValueError(f"Expected y/n but got {answer}")
    
    answer = input("Is it a daily household item? (y/n): ")
    if answer == "y":
        final_key += "1"
    elif answer == "n":
        final_key += "0"
    else:
        raise ValueError(f"Expected y/n but got {answer}")

    final_answer = items[final_key]
    print(f"Your item is {final_answer}!")


if __name__ == "__main__":
    print("Pick an item from the below list and remember it. Now answer these questions...")

    for item in items.values():
        print("  ", item)   

    run_four_questions()
