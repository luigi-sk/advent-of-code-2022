import doctest
from collections import namedtuple, OrderedDict
from pathlib import Path

TreePosition = namedtuple("TreePosition", "position, val")  # position is unique
Grid = list[list[TreePosition]]


def create_tree(line_no: int, chars: list[str]):
    return [TreePosition((line_no, char_no), int(char)) for char_no, char in enumerate(chars)]


def create_grid(lines: list[str]) -> Grid:
    return [create_tree(line_no, list(line.strip())) for line_no, line in enumerate(lines)]


def rotate_matrix(matrix: list[list]) -> list[list]:
    return list(zip(*reversed(matrix)))


def find_visible(grid: Grid):
    # rotate map from each direction
    visible_trees = set()
    for i in range(4):
        for tree_line in grid:
            max_val = -1
            for tree in tree_line:
                if max_val < tree.val:
                    max_val = tree.val
                    visible_trees.add(tree)
        grid = rotate_matrix(grid)
    return visible_trees


def puzzle1(data: str) -> int:
    """
    >>> puzzle1(Path('data/test.txt').read_text())
    21
    """
    grid = create_grid(data.splitlines())
    # pprint(grid)

    return len(find_visible(grid))


def get_up(grid: Grid, from_position: tuple[int, int]):
    """
    >>> get_up(create_grid(Path('data/test.txt').read_text().splitlines()), (0, 1))
    []
    >>> get_up(create_grid(Path('data/test.txt').read_text().splitlines()), (2, 1))
    [5, 0]
    """
    return [grid[y][from_position[1]].val for y in reversed(range(from_position[0]))]


def get_left(grid: Grid, from_position: tuple[int, int]):
    """
    >>> get_left(create_grid(Path('data/test.txt').read_text().splitlines()), (1, 0))
    []
    >>> get_left(create_grid(Path('data/test.txt').read_text().splitlines()), (1, 2))
    [5, 2]
    """
    return [grid[from_position[0]][x].val for x in reversed(range(from_position[1]))]


def get_down(grid: Grid, from_position: tuple[int, int]):
    """
    >>> get_down(create_grid(Path('data/test.txt').read_text().splitlines()), (4, 1))
    []
    >>> get_down(create_grid(Path('data/test.txt').read_text().splitlines()), (1, 2))
    [3, 5, 3]
    """
    return [grid[y][from_position[1]].val for y in range(from_position[0] + 1, len(grid))]


def get_right(grid: Grid, from_position: tuple[int, int]):
    """
    >>> get_right(create_grid(Path('data/test.txt').read_text().splitlines()), (2, 4))
    []
    >>> get_right(create_grid(Path('data/test.txt').read_text().splitlines()), (1, 1))
    [5, 1, 2]
    """
    return [grid[from_position[0]][x].val for x in range(from_position[1] + 1, len(grid[0]))]


def calc_score(heights: list[int], height_limit: int) -> int:
    _sum = 0
    for h in heights:
        if h < height_limit:
            _sum += 1
        elif h == height_limit:
            return _sum + 1
        else:
            return _sum + 1

    return _sum


def get_score_of_tree(grid: Grid, tree: TreePosition) -> int:
    scores = (calc_score(get_up(grid, tree.position), tree.val),
              calc_score(get_down(grid, tree.position), tree.val),
              calc_score(get_left(grid, tree.position), tree.val),
              calc_score(get_right(grid, tree.position), tree.val))

    return scores[0] * scores[1] * scores[2] * scores[3]


def puzzle2(data: str) -> int:
    """
    >>> puzzle2(Path('data/test.txt').read_text())
    8
    """
    grid = create_grid(data.splitlines())
    scores = OrderedDict()
    for line in grid:
        for t in line:
            scores[t.position] = get_score_of_tree(grid, t)
    # pprint(scores)
    return max(scores.values())


def main():
    # input_data = Path('data/test.txt').read_text()
    input_data = Path('data/input.txt').read_text()
    print(puzzle1(input_data))
    print(puzzle2(input_data))


if __name__ == "__main__":
    doctest.testmod()
    main()
