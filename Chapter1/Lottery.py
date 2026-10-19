from random import randint


first = int(input("Pick number 1 (1-10): "))
second = int(input("Pick number 2 (1-10): "))
third = int(input("Pick number 3 (1-10): "))


slot1 = randint(1, 10)
slot2 = randint(1, 10)
slot3 = randint(1, 10)

print("Your numbers:", first, second, third)
print("Slot result:", slot1, slot2, slot3)


if first == slot1 and second == slot2 and third == slot3:
    print("JACKPOT! You win!")
elif first == slot1 or second == slot2 or third == slot3:
    print("You got at least one right!")
else:
    print("No win, try again!")


