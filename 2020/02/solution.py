import re

# Format input spliting lower limit, upper limit, character and password
input = [re.match('(\d+)-(\d+) (\w): (\w+)', line).groups()
        for line in open('input.txt', 'r')]

# Counts the number of valid passwords
def num_valid_passwords(passwords, condition):
    count = 0

    for password in passwords:
        if condition(password):
            count += 1

    return count


# A password is valid if the character occurs n times in password
# with n in the range [lower, upper]
def part1(line):
    (lower, upper, char, password) = line
    count = 0;

    # Count number of char occurrences in password
    for c in password:
        if c == char:
            count += 1

    return int(lower) <= count <= int(upper)


print("The solution to part 1 is {}.".format(num_valid_passwords(input, part1)))


# A password is valid if exactly one of the password indices (starting at 1)
# corresponds to the letter char
def part2(line):
    (lower, upper, char, password) = line

    # Shift indices by 1
    lower, upper = int(lower) - 1, int(upper) - 1

    # Make sure exactly 1 there's only one occurrence
    return (password[lower] == char or password[upper] == char) and \
            not (password[lower] == char and password[upper] == char)


print("The solution to part 2 is {}.".format(num_valid_passwords(input, part2)))

