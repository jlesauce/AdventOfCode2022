import sys

from adventofcode.inputs.input_file import InputFile


def main() -> int:
    print('-- Day 3 --')

    part1()
    part2()

    return 0


def part1():
    common_elements_between_compartments_of_rucksacks = get_common_elements_between_compartments_of_each_rucksack()
    element_priorities = convert_elements_to_priority_values(common_elements_between_compartments_of_rucksacks)
    print(f'Answer (Part 1): {sum(element_priorities)}')


def part2():
    elves_groups = get_elves_groups()
    list_of_badges_for_each_group = find_badges_in_elves_groups(elves_groups)
    badges_priorities = convert_elements_to_priority_values(list_of_badges_for_each_group)

    print(f'Answer (Part 2): {sum(badges_priorities)}')


def get_elves_groups():
    with open(InputFile('day3.dat').path, 'r') as file:
        rucksacks = list()
        for line in file:
            rucksacks.append(list(line.rstrip()))

        group_size = 3
        elves_groups = [rucksacks[x:x + group_size] for x in range(0, len(rucksacks), group_size)]

        return elves_groups


def find_badges_in_elves_groups(elves_groups):
    elves_badges = list()
    for rucksacks_in_a_group in elves_groups:
        badge_in_a_group = get_common_elements_between_lists(rucksacks_in_a_group)
        elves_badges.append(badge_in_a_group)
    return elves_badges


def get_common_elements_between_compartments_of_each_rucksack():
    with open(InputFile('day3.dat').path, 'r') as file:
        common_elements_between_compartments = list()

        for rucksack in file:
            common_elements = get_common_elements_between_compartments_in_a_rucksack(rucksack.rstrip())
            common_elements_between_compartments.append(common_elements)

        return common_elements_between_compartments


def convert_elements_to_priority_values(common_elements_in_rucksacks):
    priority_values_of_rucksacks = list()

    for common_elements_in_a_rucksack in common_elements_in_rucksacks:
        priorities_in_a_rucksack = 0
        for element in common_elements_in_a_rucksack:
            priorities_in_a_rucksack = priorities_in_a_rucksack + to_priority_value(element)

        priority_values_of_rucksacks.append(priorities_in_a_rucksack)

    return priority_values_of_rucksacks


def to_priority_value(letter: str):
    if letter.isalpha():
        num_of_letters = ord('z') - ord('a') + 1
        shift_value = ord('A') - num_of_letters if letter.isupper() else ord('a')

        return ord(letter) - shift_value + 1
    else:
        raise ValueError(f'Input should be a letter: {letter}')


def get_common_elements_between_compartments_in_a_rucksack(rucksack: str):
    check_rucksack_is_splittable(rucksack)
    middle_index = int(len(rucksack) / 2)

    compartments = [list(rucksack[:middle_index]), list(rucksack[middle_index:])]

    return get_common_elements_between_lists(compartments)


def get_common_elements_between_lists(lists):
    return set(lists[0]).intersection(*lists)


def check_rucksack_is_splittable(rucksack: str):
    if len(rucksack) % 2 != 0:
        raise ValueError('Invalid rucksack format: size is not divisible by two')


if __name__ == '__main__':
    sys.exit(main())
