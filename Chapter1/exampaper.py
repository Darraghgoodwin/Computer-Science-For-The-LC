results = [39,32,62,88,51,62,64,81,77]

def get_grade(arithmetic_mean):
    if arithmetic_mean >= 80:
        return "Distinction"
    elif arithmetic_mean >= 70:
        return "Upper Merit"
    elif arithmetic_mean >= 60:
        return "Lower Merit"
    elif arithmetic_mean >= 50:
        return "Pass"
    else:
        return "Fail"

arithmetic_mean = sum(results) / len(results)
print(f"The mean percentage mark is {arithmetic_mean:.2f}")

grade = get_grade(arithmetic_mean)
print(f"The grade for the average result is {grade}")


# Question 16 B - Median Program

# Initialise a list of integers
# Change this list to test odd, even and empty cases
values = [27, 13, 32, 50, 16] # Sample 1 - odd
# values = [27, 13, 32, 50, 16, 29] # Sample 2 - even
# values = [] # Sample 3 - empty

# Display the initial list
print(f"The initial list of values is: {values}")

# Check if list is empty first
if len(values) == 0:
    # Display error message if list is empty
    print("The list is empty. Cannot compute the median.")
else:
    # Sort the list
    # Using sorted() to create a new sorted list
    sorted_values = sorted(values)

    # Display the sorted list
    print(f"The sorted list of values is: {sorted_values}")

    # Determine the median by examining the list length
    n = len(sorted_values)

    # Check if number of elements is odd or even
    # Odd: remainder of 1 when divided by 2
    if n % 2 == 1:
        # Odd case - middle element
        # Middle position = n // 2 (integer division)
        middle_index = n // 2
        median = sorted_values[middle_index]
    else:
        # Even case - no remainder when divided by 2
        # Mean of the two middle elements
        mid1_index = (n // 2) - 1
        mid2_index = n // 2
        # Add both middle values and divide by 2
        median = (sorted_values[mid1_index] + sorted_values[mid2_index]) / 2

    # Display the median
    print(f"The median is {median}")
