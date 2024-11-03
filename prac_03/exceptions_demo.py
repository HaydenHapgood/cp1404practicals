"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
non-integar inputs (decimals) will cause a valueerror
2. When will a ZeroDivisionError occur?
When denominator = 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Put a  while loop to check for a denominator of 0 and repeat until a non-zero integar is used
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Invalid denominator, cannot divide by zero.")
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")