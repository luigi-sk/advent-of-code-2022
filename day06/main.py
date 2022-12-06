import doctest
from pathlib import Path


def puzzle1(data: str) -> int:
    """
    >>> puzzle1('bvwbjplbgvbhsrlpgdmjqwftvncz')
    5
    >>> puzzle1('nppdvjthqldpwncqszvftbrmjlhg')
    6
    >>> puzzle1('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
    10
    >>> puzzle1('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
    11
    """
    return 4 + next(idx for idx, _ in enumerate(list(data)) if len(set(data[idx:idx+4])) == 4)


def puzzle2(data: str) -> int:
    """
    >>> puzzle2('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
    19
    >>> puzzle2('bvwbjplbgvbhsrlpgdmjqwftvncz')
    23
    >>> puzzle2('nppdvjthqldpwncqszvftbrmjlhg')
    23
    >>> puzzle2('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
    29
    >>> puzzle2('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
    26
    """
    return 14 + next(idx for idx, _ in enumerate(list(data)) if len(set(data[idx:idx+14])) == 14)


def main():
    # input_data = Path("data/test.txt").read_text()
    input_data = Path("data/input.txt").read_text()
    print(puzzle1(input_data))
    print(puzzle2(input_data))


if __name__ == "__main__":
    doctest.testmod()
    main()
