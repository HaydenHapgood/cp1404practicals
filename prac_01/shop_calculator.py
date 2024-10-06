# number of items
#price of item n
# Total price
# if total over 100$ 10% discount
total = 0
items = 0
while items <= 0:
    items = int(input("How many items are you purchasing? :"))
    if items > 0:
            for i in range(items):
                cost = float(input(f"Cost of item {i+1}: $"))
                total += cost
            print(f"Your total is: ${total:.2f}")
            if total >= 100:
                discount = 0.1
                print(f"Your total is over $100.00, you are eligible for a 10% discount!")
            else:
                discount = 0
            total_cost = total - total*discount
            print(f"Your final total is: ${total_cost:.2f}")
    else:
        print("Invalid number of items. Please try again.")
