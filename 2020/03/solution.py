# Matrix with the map, repeating the pattern 100 times
input = [100*line.rstrip() for line in open("input.txt", "r")]

# Determines if the position has a tree
def is_tree(position):
    return position == '#'

# Counts the number of trees encountered while following
# the moviment (right) squares to the right, (down) squares down
def tree_counter(map, right, down):
    line, column = 0, 0; lines = len(map); curr_line = map[line]
    num_tree = 0

    # While the last line isn't reached
    while line + down < lines:
        line += down; column += right; current = map[line]
        if is_tree(current[column]):
            num_tree += 1

    return num_tree

# Counts the number of trees if the followed path is
# 3 right and 1 down
def part1(map):
    return tree_counter(map, 3, 1)

print("The solution to part 1 is {}.".format(part1(input)))


# Returns the product of the trees found traversing the map
# with the speficied slopes
def part2(map):
    mul = part1(map)

    for (right, down) in ((1, 1), (5, 1), (7, 1), (1, 2)):
        mul *= tree_counter(map, right, down)

    return mul

print("The solution to part 2 is {}.".format(part2(input)))

