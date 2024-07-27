#hello
cards = ["AS", "2S"]
community = ["3S", "4S", "5S", "6S", "7S"]
conversions = {"A": 1, "J": 11, "Q": 12, "K": 13} 

numbers = []
for x in cards, community:
  y = x[1:]
  if y in conversions:
    numbers.append(conversions[y])
  else:
    numbers.append(int(y))
print(numbers)
