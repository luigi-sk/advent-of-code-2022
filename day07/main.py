import doctest
import os
from collections import Counter, OrderedDict
from os import path
from pathlib import Path


def parse_files(lines):
    cwd: str = ""
    files = OrderedDict()
    for line in lines:
        match line.strip().split(" "):
            case ["$", "cd", cd_path]:
                cwd = path.normpath(path.join(cwd, cd_path))
            case ["$", "ls"]:
                pass
            case ["dir", dirname]:
                pass
            case [size, filename] if size.isdigit():
                filepath = path.join(cwd, filename)
                files[filepath] = int(size)
            case ['']:  # empty line
                pass
            case _:
                raise ValueError(f"Unknown cmd '{line}'")
    return files


def get_folders_of_path(filepath: str) -> list[str]:
    without_file = filepath.split(os.sep)[:-1]
    return [path.join(os.sep, *without_file[:i+1]) for i in range(len(without_file))]


def get_folders_size(files) -> Counter:
    counter = Counter()
    for filepath, size in files.items():
        counter += Counter(**{folder: size for folder in get_folders_of_path(filepath)})
    return counter


def puzzle1(data: str) -> int:
    """
    >>> puzzle1(Path("data/test.txt").read_text())
    95437
    """
    lines = data.split("\n")
    counter = get_folders_size(parse_files(lines))
    dirs_under_100k = {dirname: size for dirname, size in counter.items() if size <= 100_000}
    return sum(dirs_under_100k.values())


def puzzle2(data: str) -> int:
    """
    >>> puzzle2(Path("data/test.txt").read_text())
    24933642
    """
    lines = data.split("\n")
    counter = get_folders_size(parse_files(lines))
    free_up_space = 30000000 - (70000000 - counter["/"])
    dirs_to_delete = {dirname: size for dirname, size in counter.items() if size >= free_up_space}
    dirs_to_delete = OrderedDict(sorted(dirs_to_delete.items(), key=lambda item: item[1]))

    return next(iter(dirs_to_delete.values()))


def main():
    # input_data = Path("data/test.txt").read_text()
    input_data = Path("data/input.txt").read_text()
    print(puzzle1(input_data))
    print(puzzle2(input_data))


if __name__ == "__main__":
    doctest.testmod()
    main()
