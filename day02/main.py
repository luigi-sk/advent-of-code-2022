import dataclasses
from typing import List, Self, Sequence

PLAY_WIN = 6
PLAY_DRAW = 3
PLAY_LOOSE = 0


@dataclasses.dataclass
class Shape:
    name: str
    score: int
    stronger_than: List[Self]

    def play(self, other: Self) -> int:
        play_score = self.play_score(other)
        return self.score + play_score

    def play_score(self, other):
        if self == other:
            return PLAY_DRAW

        return PLAY_WIN if other in self.stronger_than else PLAY_LOOSE


ShapeInput = Sequence[tuple[Shape, Shape]]


PAPER = Shape("PAPER", 2, [])
ROCK = Shape("ROCK", 1, [])
SCISSORS = Shape("SCISSORS", 3, [])
SHAPES = (PAPER, ROCK, SCISSORS)

PAPER.stronger_than = [ROCK]
PAPER.advice_result = {

}
ROCK.stronger_than = [SCISSORS]
SCISSORS.stronger_than = [PAPER]

TRANSLATIONS = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
}


def translate(input_str: tuple[str, ...]) -> tuple[Shape, Shape]:
    player, me = input_str
    return TRANSLATIONS[player], TRANSLATIONS[me]


def process_input(filename: str) -> ShapeInput:
    with open(filename, "r") as f:
        return [translate(tuple(line.split(" "))) for line in f.read().splitlines()]


def puzzle1(data: ShapeInput) -> int:
    return sum([me.play(opponent) for opponent, me in data])


def draw(shape: Shape) -> Shape:
    return shape


def win(shape: Shape) -> Shape:
    return next(_shape for _shape in SHAPES if _shape.play_score(shape) == PLAY_WIN)


def loose(shape: Shape) -> Shape:
    return next(_shape for _shape in SHAPES if _shape.play_score(shape) == PLAY_LOOSE)


STRATEGIES = {
    ROCK.name: loose,
    PAPER.name: draw,
    SCISSORS.name: win,
}


def puzzle2(data: ShapeInput) -> int:
    result = 0
    for opponent, advice in data:
        play = STRATEGIES[advice.name](opponent).play(opponent)
        result += play
    return result
    # return sum([STRATEGIES[advice.name](opponent).play(opponent) for opponent, advice in data])


def show_results(name: str, test_results, expected_test: int, input_results):
    assert test_results == expected_test
    print(f"{name} test: {test_results}")
    print(f"{name} input: {input_results}")
    print("----------------------------------------------------------------")


def main():
    data_test = process_input("data/test.txt")
    data_input = process_input("data/input.txt")

    show_results("Puzzle 1", puzzle1(data_test), 15, puzzle1(data_input))
    show_results("Puzzle 2", puzzle2(data_test), 12, puzzle2(data_input))


if __name__ == "__main__":
    main()
