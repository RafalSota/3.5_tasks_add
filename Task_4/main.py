dice = {}

for dice_one in range(1,7):
    for dice_two in range(1,7):
        sum = dice_one + dice_two
        #print(dice_one, dice_two, sum)
        dice.setdefault(sum, set())     #tworzy słownik: key to suma wszystkich możliwych sum dwóch rzutów kostką (2-12), value to pusty zbiór 
        dice[sum].add((dice_one, dice_two))   #tworzy krotkę jako pojedynczy element i dodaje do słownika bez dublowania (właściwość zbioru)

print("\nPełny słownik wszystkich możliwości rzutu dwoma kostkami:\n")
import pprint
pprint.pprint(dice) 

print(f"\nWszystkie możliwości dla sumy oczek 7: {dice[7]}\n")
print(f"\nWszystkie możliwości dla sumy oczek 9: {dice[9]}\n")

"""kod kodilla
dice = {}
for i in range(1,7):
  for j in range (1,7):
    dice.setdefault(i+j,set())
    dice[i+j].add((i,j))
print(dice[7])
"""
