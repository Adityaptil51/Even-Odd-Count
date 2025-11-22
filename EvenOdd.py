import sys

if len(sys.argv) < 2:
    print("Usage: python even_odd.py <num1> <num2> <num3> ...")
    sys.exit(1)

numbers = list(map(int, sys.argv[1:]))

even_count = 0
odd_count = 0

for n in numbers:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Count of Even Numbers:", even_count)
print("Count of Odd Numbers:", odd_count)
