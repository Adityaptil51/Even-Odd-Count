import sys

if len(sys.argv) != 2:
    print("Usage: <NUMBERS>")
    sys.exit(1)

try:
    numbers = list(map(int, sys.argv[1].split(',')))
except ValueError:
    print("ERROR: Only integers allowed.")
    sys.exit(1)

# Check for 2 or 3 numbers
if len(numbers) < 2 or len(numbers) > 3:
    sys.exit(1)

print("Numbers:", numbers)

even_count = sum(1 for n in numbers if n % 2 == 0)
odd_count = len(numbers) - even_count

print("Count of Even Numbers:", even_count)
print("Count of Odd Numbers:", odd_count)
