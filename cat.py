# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat1 = Cat("Bob", 8)
cat2 = Cat("Roger", 7)
cat3 = Cat("Albert", 17)


# 2 Create a function that finds the oldest cat
ageList = [cat1.age, cat2.age, cat3.age]


def oldestCat():
    oldest = ageList[0]
    for cat in ageList:
        if cat > oldest:
            oldest = cat
    return oldest


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print("The oldest cat is " + str(oldestCat()))
