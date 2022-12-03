import dataclasses
from itertools import zip_longest
from typing import List


@dataclasses.dataclass
class Rucksack:
    compartments: tuple[str, str]

    def __init__(self, items: str) -> None:
        comp_size = int(len(items) / 2)
        self.compartments = items[:comp_size], items[-comp_size:]

    def contains_both(self) -> str:
        return "".join(
            set(self.compartments[0]) & set(self.compartments[1])
        )

    def items_set(self):
        return set("".join(self.compartments))


def item_score(item:str) -> int:
    return ord(item[0]) - (96 if item[0].islower() else 38)


Rucksacks = List[Rucksack]


def process_input(filename: str) -> Rucksacks:
    with open(filename, "r") as f:
        return [Rucksack(line.strip()) for line in f.readlines()]


def puzzle1(data: Rucksacks):
    return sum([item_score(rucksack.contains_both()) for rucksack in data])


def puzzle2(data: Rucksacks):
    group_in = [iter(data)] * 3
    groups = zip_longest(*group_in)
    badges = [set.intersection(*list(map(lambda x: x.items_set(), group))) for group in groups]
    return sum([item_score("".join(badge)) for badge in badges])


def show_results(name: str, test_results, expected_test: int, input_results):
    assert test_results == expected_test
    print(f"{name} test: {test_results}")
    print(f"{name} input: {input_results}")
    print("----------------------------------------------------------------")


def main():
    data_test = process_input("data/test.txt")
    data_input = process_input("data/input.txt")

    show_results("puzzle1", puzzle1(data_test), 157, puzzle1(data_input))
    show_results("puzzle2", puzzle2(data_test), 70, puzzle2(data_input))

    puzzle2(data_test)


if __name__ == "__main__":
    main()