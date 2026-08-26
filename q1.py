n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    numbers.append(value)
    largest = numbers[0]
smallest = numbers[0]
total = 0
even_count = 0
odd_count = 0

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    total = total + num
    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Largest:", largest)
print("Smallest:", smallest)
print("Sum:", total)
print("Even count:", even_count)
print("Odd count:", odd_count)
reversed_list = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Reversed:", reversed_list)