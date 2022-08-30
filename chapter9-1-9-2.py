def good():
    return ['Harry', 'Ron', 'Hermione']


print(good())

odds = []


def get_odds():
    for i in range(10):
        if i % 2 != 0:
            odds.append(i)
    return odds


odds = get_odds()
print(odds[2])
