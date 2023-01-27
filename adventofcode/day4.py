import sys

from adventofcode.inputs.input_file import InputFile


def main() -> int:
    print('-- Day 4 --')

    pair_assignments = part1()
    part2(pair_assignments)

    return 0


def part1():
    pair_assignments = get_pair_assignments()
    overlapping_assignments = find_overlapping_assignments(pair_assignments, is_fully_overlapping)
    print(f'Answer (Part 1): {len(overlapping_assignments)}')

    return pair_assignments


def part2(pair_assignments):
    overlapping_assignments = find_overlapping_assignments(pair_assignments, is_simply_overlapping)
    print(f'Answer (Part 1): {len(overlapping_assignments)}')


def get_pair_assignments():
    with open(InputFile('day4.dat').path, 'r') as file:
        pair_assignments = list()
        for assignment in file:
            pair_sections_range = assignment.rstrip().split(',')
            pair_sections_indexes = [[int(value) for value in range_.split('-')] for range_ in pair_sections_range]

            pair_assignments.append(pair_sections_indexes)

        return pair_assignments


def find_overlapping_assignments(pair_assignments, overlapping_method):
    overlapping_assignments = list()
    for pair in pair_assignments:
        if overlapping_method(pair[0], pair[1]):
            overlapping_assignments.append(pair)
    return overlapping_assignments


def is_fully_overlapping(section0, section1):
    return section0[0] >= section1[0] and section0[1] <= section1[1] \
        or section1[0] >= section0[0] and section1[1] <= section0[1]


def is_simply_overlapping(section0, section1):
    section0_range = range(section0[0], section0[1] + 1)
    section1_range = range(section1[0], section1[1] + 1)

    return section0[0] in section1_range or section0[1] in section1_range \
        or section1[0] in section0_range or section1[1] in section0_range


if __name__ == '__main__':
    sys.exit(main())
