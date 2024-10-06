"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales: float = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = 10
        total = sales * (bonus/100)
        print(f'Your bonus is {bonus}%, and comes to: ${total:.2f}')
        sales: float = float(input("Enter sales: $"))
    elif sales >= 1000:
        bonus = 15
        total = sales * (bonus/100)
        print(f'Your bonus is {bonus}%, and comes to: ${total:.2f}')
        sales: float = float(input("Enter sales: $"))
