# List 
num = [1,2,3,4,5,6,7,8,9,10]

# 
def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

print("The list of numbers is:", num)
average = average(num)
print(f"The average of the elements is: {average}")
