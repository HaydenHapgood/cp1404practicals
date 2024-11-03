from guitar import Guitar
guitars = []
while True:
    name = input("Name (press Enter to finish): ")
    if name == "":
        break
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)

print("\nThese are my guitars:")
for index, guitar in enumerate(guitars, 1):
    vintage_check = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {index}: {guitar.name} ({guitar.year}), worth ${guitar.cost:,.2f} {vintage_check}")
