#Task1
for y in range(1,11):
    print(y)
    
counter = 1
while(counter < 5):
    print(counter)
    counter+=1
while(counter < 5):
    print(counter)
    counter+=1
    print(counter)
    
#Task 2
number = int(input("Enter a number:"))
for y in range(1,number):
    print(y)
    
#task3
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = 0

for char in sentence:
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")

Task 4
sentence = input("Enter a sentence: ")
reversed_sentence = ""

for char in sentence:
    reversed_sentence = char + reversed_sentence  # adds char to front

print(reversed_sentence)

Task 5
sentence = input("Enter a sentence: ")
letter = input("Enter a single character: ")

count = 0
for char in sentence:
    if char == letter:
        count += 1

print(f"'{letter}' appears {count} times in the sentence.")

