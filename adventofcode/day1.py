import sys
from pathlib import Path

from adventofcode.inputs.input_file import InputFile


def main() -> int:
    print('-- Day 1 --')

    elves_calories = part1()
    part2(elves_calories)

    return 0


def part1() -> list:
    elves_calories = collect_all_elves_calories(InputFile('day1.dat').path)
    elf_index_with_max_calories = elves_calories.index(max(elves_calories))

    print(f'Elf with highest calories amount is {elf_index_with_max_calories},'
          f'who has {elves_calories[elf_index_with_max_calories]} calories.')

    print(f'\nAnswer (Part 1): {elves_calories[elf_index_with_max_calories]}\n')

    return elves_calories


def part2(elves_calories: list):
    print('The top 3 of the highest amount of calories is:\n'
          f'1. {elves_calories[0]}\n'
          f'2. {elves_calories[1]}\n'
          f'3. {elves_calories[2]}')

    print('')
    print(f'Answer (Part 2): {sum(elves_calories[0:3])}')


def collect_all_elves_calories(input_file_path: Path) -> list:
    elves_calories = []
    with open(input_file_path, 'r') as file:

        current_elf = 0
        for line in file:
            line = line.rstrip()
            if line:
                current_elf = current_elf + int(line)
            else:
                if current_elf != 0:
                    elves_calories.append(current_elf)
                    current_elf = 0
        if current_elf != 0:
            elves_calories.append(current_elf)
    return elves_calories


if __name__ == '__main__':
    sys.exit(main())
