from score import check_score

def main():
    score = None
    choice = ""

    while choice != "Q":
        print("(G)et score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input(">>> ")

        if choice == "G":
                score = int(input('Enter score (0-100): '))
                if score < 0 or score > 100:
                    print('Invalid score.')
                else:
                    print('Your score has been saved.')

        elif choice == "P":
            if score != None:
                result = check_score(score)
                print('Your score is:', result)
            else:
                print('No score saved.')

        elif choice == "S":
            if score != None:
                print('*' * score)
            else:
                print('No score saved.')

        elif choice == "Q":
            print("Thank you for using this program.")

        else:
            print("Invalid input")
main()
