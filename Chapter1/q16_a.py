#Question 16 C

def get_grade(result):
   #Part iii Completion of grade indicaters 
    if result >= 80:
        grade = "Distinction"
    elif result >= 65:
        grade = "Upper Merit"
    elif result >= 50:
        grade = "Lower Merit"
    elif result >=40:
        grade = "pass"
    else:
         grade = "Unsuccessful"
        
    return grade

results = [39,32,62,88,51,62,64,81,77] 
N = len(results)
total = 0

for i in range(N):
    total = total + results[i]
#i part one addingbrackets then putting round infront and an arguement to 2 decimal places.
#ii adding N instead of 9, as N counts the length of results.   
arithmetic_mean = round(total/N,2)

print("The mean percentage mark is", arithmetic_mean)
#iv
gradeIndicater = get_grade(arithmetic_mean)
print("The grade for the average result is",gradeIndicater)




