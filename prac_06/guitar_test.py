from guitar import Guitar

test_guitar1 = Guitar("Gibson L-5 CES",1922,16035.40)
test_guitar2 = Guitar("Another Guitar",2013,1)

test_age1 = test_guitar1.get_age()
test_vintage1 = test_guitar1.is_vintage()

test_age2 = test_guitar2.get_age()
test_vintage2 = test_guitar2.is_vintage()

print(f"{test_guitar1.name} get_age() - Expected 100. Got {test_age1}")
print(f"{test_guitar1.name} is_vintage() - Expected True. Got {test_vintage1}")

print(f"{test_guitar2.name} get_age() - Expected 9. Got {test_age2}")
print(f"{test_guitar2.name} is_vintage() - Expected False. Got {test_vintage2}")