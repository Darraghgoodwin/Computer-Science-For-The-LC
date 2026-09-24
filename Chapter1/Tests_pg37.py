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
v = input("Enter a Word:")
vowelCount = 0
for character in v:
    if character =="a,e,i,o,u":
     vowelCount+=1
# wordCount = vowelCount+1
print("Vowels:", vowelCount)
# print("Words: ", wordCount)
#     
