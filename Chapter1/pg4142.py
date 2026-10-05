Task 1 - Add 1 to each item
numbers = []

for i in range(5):
    n = int(input(f"Enter number {i+1}: "))
    numbers.append(n)

print("Original list:", numbers)

separately add 1 to each item
for i in range(len(numbers)):
    numbers[i] = numbers[i] + 1

print("Incremented list:", numbers)

Task 2 - Stephen's milk
hours = []

input 7 days - you can also just use hours = [12,7,9,9,6,8,2]
for i in range(7):
    h = int(input(f"Enter waking hours at home for Day {i+1}: "))
    hours.append(h)

given in book: [12, 7, 9, 9, 6, 8, 2]
hours = [12, 7, 9, 9, 6, 8, 2]
total_hours = sum(hours)
total_milk = total_hours * 0.5 # 0.5 litres per hour
cost = total_milk * 1.35

print(f"\nTotal hours at home: {total_hours} hours")
print(f"Total milk drunk: {total_milk} litres")
print(f"Amount Stephen must pay his father: €{cost:.2f}")

Task 3 - Rainfall
rainfall = []

input 7 days into list
for i in range(7):
    amount = float(input(f"Enter rainfall for Day {i+1} in cm: "))
    rainfall.append(amount)

calculate total and average
total = sum(rainfall)
average = total / len(rainfall)

print(f"\nTotal rainfall for the week: {total:.1f} cm")
print(f"Average rainfall: {average:.2f} cm")

separate loop for heavy rainfall
for i in range(7):
    if rainfall[i] > 3.5:
        print(f"Warning: Heavy rainfall on Day {i+1}: {rainfall[i]} cm exceeded 3.5 cm")

Task 4 - Shoe shop sales analysis
names = []
sales = []

num = int(input("Enter number of salespeople: "))

for i in range(num):
    name = input(f"Enter name of salesperson {i+1}: ")
    value = float(input(f"Enter sales for {name} in euro: "))
    names.append(name)
    sales.append(value)

print("\n--- Sales Report ---")
for i in range(num):
    print(f"{names[i]}: €{sales[i]:.2f}")

total_sales = sum(sales)
print(f"\nTotal sales by all: €{total_sales:.2f}")
print(f"Maximum sales: €{max(sales):.2f}")
print(f"Minimum sales: €{min(sales):.2f}")
print(f"Average sales per person: €{total_sales/num:.2f}")

optional: who had max/min
max_index = sales.index(max(sales))
print(f"Top salesperson: {names[max_index]}")
