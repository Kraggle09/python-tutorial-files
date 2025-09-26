animals = ["cat", "dog", "bird"]
print(animals) # Output: ['cat', 'dog', 'bird']
print(animals[0]) # Output: cat
animals.append("horse")

highScoreOwners = ["Jake", "Sarah"]
print(highScoreOwners) # Output: ['Jake', 'Sarah']
highScoreOwners.insert(1, "Michael")
print(highScoreOwners) # Output: ['Jake', 'Michael', 'Sarah']

currentSubscriptionHolders = ["Michelle", "John", "Clint"]
print(currentSubscriptionHolders) # Output: ['Michelle', 'John', 'Clint']
currentSubscriptionHolders.remove("John") # Removes the first item with a value of "John"
print(currentSubscriptionHolders) # Output: ['Michelle', 'Clint']

currentSubscriptionHolders = ["Michelle", "John", "Clint"]
print(currentSubscriptionHolders) # Output: ['Michelle', 'John', 'Clint']
currentSubscriptionHolders.pop(1) # Removes the item at index 1
print(currentSubscriptionHolders) # Output: ['Michelle', 'Clint']


planOptions = ("basic", "plus", "premiere")
print(planOptions[1])


favoriteAnimals = {"Janet": "cat", "Ann": "dog", "Doug": "bird"}
print(favoriteAnimals["Ann"]) # Output: dog
favoriteAnimals["Frank"] = "horse"
favoriteAnimals.pop("Janet")