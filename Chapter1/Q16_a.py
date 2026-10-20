#Question 16 (a)
#Examination Number:123456
from random import choice

fruits = ["apple", "cherry","orange"]

random_fruits_1 = choice(fruits)
#(ii)
random_fruits_2 = choice(fruits)
random_fruits_3 = choice(fruits)
#(i)
print("Random Fruit 1:",random_fruits_1)
#(ii)
print("Random Fruit 2:", random_fruits_2)
print("Random Fruit 3:",random_fruits_3 )

#(iii)
print("First Fruit is", random_fruits_1)

#(iv)
if random_fruits_1 == random_fruits_2:
    print("First pair match")
   #(vi) 
elif random_fruits_3 == random_fruits_1:
    print("Matching pair")
    
elif random_fruits_3 == random_fruits_2:
    print("Matching pair")
    
#(vii)

