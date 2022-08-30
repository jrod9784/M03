from ast import Delete
from dataclasses import replace


things = ["mozzarella", "cinderella", "salmonella"]
things[1].capitalize()
print(things)
# did not capitalize, however:
print(things[1].capitalize())
# does
things[0].upper()
print(things)
print(things[0].upper())
things[0] = things[0].upper()
print(things)

things.remove(things[2])
print(things)
