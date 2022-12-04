from utils import results

Assigment = set[int]
Pairs = tuple[Assigment, Assigment]


def create_assigment(range_str: str)->Assigment:
    _from, _to = map(int, range_str.split("-"))
    return set(range(_from, _to+1))


def create_pairs(line: str)->Pairs:
    e1, e2 = line.split(",")
    return create_assigment(e1), create_assigment(e2)


def process_input(filename) -> list[Pairs]:
    with open(filename, 'r') as reader:
        lines = reader.readlines()
        pairs = [create_pairs(line) for line in lines if line.strip()]
    return pairs


def puzzle1(data: list[Pairs]) -> int:
    return sum([1 for e1, e2 in data if e1.issubset(e2) or e2.issubset(e1)])


def puzzle2(data: list[Pairs]) -> int:
    return sum([1 for e1, e2 in data if set.intersection(e1, e2)])


def main():
    data_test = process_input("data/test.txt")
    data_input = process_input("data/input.txt")

    results.show("p1", puzzle1(data_test), 2, puzzle1(data_input))
    results.show("p1", puzzle2(data_test), 4, puzzle2(data_input))


if __name__ == "__main__":
    main()
