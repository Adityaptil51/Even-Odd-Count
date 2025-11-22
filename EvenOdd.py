import sys

if len(sys.argv) == 2:
    numbers = list(map(int, sys.argv[1].split(',')))
    print("Numbers received from Jenkins parameter:", numbers)
    sys.exit(1)
else:
    numbers = [1, 2, 3, 4, 5, 6]
    print("No Jenkins parameter provided. Using default numbers:", numbers)

even_count = sum(1 for n in numbers if n % 2 == 0)
odd_count = len(numbers) - even_count

print("Count of Even Numbers:", even_count)
print("Count of Odd Numbers:", odd_count)
