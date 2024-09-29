
name = input("Enter name: ")
choice = 0
while choice != "Q":
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>>")
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    elif choice == "Q":
        print("Finished")
    else:
        print("Invalid input")
