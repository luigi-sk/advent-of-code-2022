import doctest
from collections import deque, OrderedDict
from pathlib import Path

Stack = deque[str]
Stacks = OrderedDict[str, Stack]


def create_stack_from_line(line: tuple[str, ...]) -> Stack:
    return deque(list("".join(line).strip()[1:]))


def create_stacks(str_def) -> Stacks:
    matrix = [list(line) for line in str_def.split("\n")]
    # pprint(matrix)
    matrix = list(zip(*reversed(matrix)))  # rotate array
    stacks = OrderedDict()
    for line in matrix:
        if line[0].strip():
            stacks[line[0].strip()] = create_stack_from_line(line)
    # pprint(stacks)
    return stacks


def make_move(stacks, size, from_id, to_id):
    for _ in range(size):
        stacks[to_id].append(stacks[from_id].pop())


def make_move_v2(stacks, size, from_id, to_id):
    stacks[to_id].extend(
        reversed([stacks[from_id].pop() for _ in range(size)])
    )


def puzzle1(data: str):
    """
    >>> puzzle1(Path("data/test.txt").read_text())
    'CMZ'
    """
    crane_def, instructions = data.split('\n\n')
    stacks = create_stacks(crane_def)
    for instruction in instructions.split("\n"):
        cmd, size, _, from_id, _, to_id = instruction.split(' ')
        make_move(stacks, int(size), from_id, to_id)
    return "".join([stack.pop() for stack in stacks.values()])


def puzzle2(data: str):
    """
    >>> puzzle2(Path("data/test.txt").read_text())
    'MCD'
    """
    crane_def, instructions = data.split('\n\n')
    stacks = create_stacks(crane_def)
    for instruction in instructions.split("\n"):
        cmd, size, _, from_id, _, to_id = instruction.split(' ')
        make_move_v2(stacks, int(size), from_id, to_id)
    return "".join([stack.pop() for stack in stacks.values()])


def main():
    # input_data = Path("data/test.txt").read_text()
    input_data = Path("data/input.txt").read_text()
    print(puzzle1(input_data))
    print(puzzle2(input_data))


if __name__ == "__main__":
    doctest.testmod()
    main()
