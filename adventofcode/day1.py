import sys
from pathlib import Path

from adventofcode.inputs.input_file import InputFile


def main() -> int:
    print('-- Day 1 --')

    elves_calories = collect_all_elves_calories(InputFile('day1.dat').path)
    elf_index_with_max_calories = elves_calories.index(max(elves_calories))

    print(f'Elf with highest calories amount is {elf_index_with_max_calories},'
          f'who has {elves_calories[elf_index_with_max_calories]} calories.')

    print('')
    print(f'Answer: {elves_calories[elf_index_with_max_calories]}')
    return 0


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
