
def check_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

import random

def main():
    score = float(input("Enter score: "))
    result = check_score(score)
    print(result)

    random_score = random.randint(1, 100)
    print('Random score:', random_score)
    random_result = check_score(random_score)
    print(random_result)

# used ai to help get this part, looked over very briefly in the lectures.
# causes the main function to only execute when this file is executed, allowing the use of check_score in menu
if __name__ == "__main__":
    main()