import sys
from enum import Enum

from adventofcode.inputs.input_file import InputFile


class HandShape(str, Enum):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSOR = 'scissor'

    @staticmethod
    def to_hand_shape(shape_str: str):
        if shape_str.lower() in ['rock', 'a', 'x']:
            return HandShape.ROCK
        elif shape_str.lower() in ['paper', 'b', 'y']:
            return HandShape.PAPER
        elif shape_str.lower() in ['scissor', 'c', 'z']:
            return HandShape.SCISSOR
        else:
            raise ValueError(f'Invalid enum value: {shape_str}')


class RoundOutcome(int, Enum):
    DEFEAT = 0,
    EQUALITY = 3,
    VICTORY = 6


HAND_SHAPE_POINTS = {
    HandShape.ROCK: 1,
    HandShape.PAPER: 2,
    HandShape.SCISSOR: 3,
}

EXPECTED_OUTCOME_FROM_CHAR_VALUE = {
    'X': RoundOutcome.DEFEAT,
    'Y': RoundOutcome.EQUALITY,
    'Z': RoundOutcome.VICTORY
}

HAND_SHAPES_OUTCOME_MATRIX = {
    HandShape.ROCK: {
        HandShape.ROCK: RoundOutcome.EQUALITY,
        HandShape.PAPER: RoundOutcome.DEFEAT,
        HandShape.SCISSOR: RoundOutcome.VICTORY,
    },
    HandShape.PAPER: {
        HandShape.ROCK: RoundOutcome.VICTORY,
        HandShape.PAPER: RoundOutcome.EQUALITY,
        HandShape.SCISSOR: RoundOutcome.DEFEAT,
    },
    HandShape.SCISSOR: {
        HandShape.ROCK: RoundOutcome.DEFEAT,
        HandShape.PAPER: RoundOutcome.VICTORY,
        HandShape.SCISSOR: RoundOutcome.EQUALITY,
    },
}


def main() -> int:
    print('-- Day 2 --')

    part1()
    part2()

    return 0


def part1():
    total_score = 0
    with open(InputFile('day2.dat').path, 'r') as file:
        for round_str in file:
            round_str = round_str.rstrip()

            total_score = total_score + compute_round_points_part_1(round_str)

    print(f'Answer (Part 1): {total_score}\n')


def part2():
    total_score = 0
    with open(InputFile('day2.dat').path, 'r') as file:
        for round_str in file:
            round_str = round_str.rstrip()

            total_score = total_score + compute_round_points_part_2(round_str)

    print(f'Answer (Part 2): {total_score}\n')


def get_string_tokens(value: str):
    tokens = value.split(sep=' ')

    if not len(tokens) == 2:
        raise ValueError(f'Invalid round input: {value}')
    return tokens[0], tokens[1]


def compute_round_points_part_1(round_str: str) -> int:
    opponent_hand_str, my_hand_str = get_string_tokens(round_str)

    opponent_hand = HandShape.to_hand_shape(opponent_hand_str)
    our_hand = HandShape.to_hand_shape(my_hand_str)

    round_outcome = compute_round_outcome(our_hand, opponent_hand)

    return HAND_SHAPE_POINTS[our_hand] + round_outcome.value


def compute_round_points_part_2(round_str: str) -> int:
    opponent_hand_str, expected_outcome_str = get_string_tokens(round_str)

    opponent_hand = HandShape.to_hand_shape(opponent_hand_str)
    expected_outcome = EXPECTED_OUTCOME_FROM_CHAR_VALUE[expected_outcome_str]

    what_to_play = next(hand_shape for hand_shape in HAND_SHAPES_OUTCOME_MATRIX[opponent_hand].keys() if
                        HAND_SHAPES_OUTCOME_MATRIX[hand_shape][opponent_hand] == expected_outcome)

    round_outcome = compute_round_outcome(what_to_play, opponent_hand)

    return HAND_SHAPE_POINTS[what_to_play] + round_outcome.value


def compute_round_outcome(player1_hand: HandShape, player2_hand: HandShape) -> RoundOutcome:
    return HAND_SHAPES_OUTCOME_MATRIX[player1_hand][player2_hand]


if __name__ == '__main__':
    sys.exit(main())
