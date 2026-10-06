#Task 1 
numbers = []

for i in range(5):
    n = int(input("Enter number: "))
    numbers.append(n)

print("Original list:", numbers)


for i in range(len(numbers)):
    numbers[i] = numbers[i] + 1

print("Incremented list:", numbers)

#Task 2 
hours = []


for i in range(7):
    h = int(input("Enter waking hours at home for Day: "))
    hours.append(h)


hours = [12, 7, 9, 9, 6, 8, 2]
total_hours = sum(hours)
total_milk = total_hours * 0.5 
cost = total_milk * 1.35

print("\nTotal hours at home:", total_hours )
print("Total milk drunk:", total_milk litres)
print("Amount Stephen must pay his father:", cost)

#Task 3
rainfall = []


for i in range(7):
    amount = float(input("Enter rainfall for Day: "))
    rainfall.append(amount)


total = sum(rainfall)
average = total / len(rainfall)

print("Total rainfall for the week:", total )
print("Average rainfall:", average )


for i in range(7):
    if rainfall[i] > 3.5:
        print("Warning: Heavy rainfall on Day exceeded 3.5 cm")


