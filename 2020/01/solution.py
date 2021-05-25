# List of numbers of the puzzle input
input = [int(n) for n in open("input.txt", "r")]

# Find two numbers that sum to the given sum,
# returning their product.
def part1(input, sum):
    for n in input:
        if sum-n in input:
            return n * (sum-n)


# Find three numbers that sum to the given sum,
# returning their product.
def part2(input, sum):
    for n in input:
        mul = part1(input, sum-n)
        if mul:
            return mul * n

print("The solution to part 1 is {}.".format(part1(input, 2020)))
print("The solution to part 2 is {}.".format(part2(input, 2020)))
