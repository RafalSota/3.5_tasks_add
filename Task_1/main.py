numbers = [5,32,56,2,2,16,7,10,23,100]
mean_number = 0

print(f"\nLista numbers: {numbers}")
numbers = [(number+5)//10*10 for number in numbers]
print(f"Lista numbers po zaokrągleniu liczb do dziesitek w górę: {numbers}")

""" kod kodilla
for i,n in enumerate(numbers):
  tens = n//10
  remainder = 10 if n%10 >= 5 else 0
  numbers[i] = tens*10 + remainder
"""

maksimum = max(numbers)
minimum = min(numbers)

for i in range(len(numbers)-1, 0, -1):
  if numbers[i] == minimum or numbers[i] == maksimum:
    del numbers[i]
print(f"Lista numbers po usunięciu wszystkich maksimum i minimum: {numbers}")

"""kod kodilla - usuwa tylko jeden element o wartości min lub max
numbers.remove(min(numbers))
numbers.remove(max(numbers))
"""

for number in numbers:
  mean_number += number
mean_number = round(mean_number / len(numbers),2)
print(f"Średnia z listy numbers: {mean_number}\n")

"""kod kodilla
mean_number = sum(numbers) / len(numbers)
print(mean_number)
"""



