import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# INPUT_FILE = "example.txt"
INPUT_FILE = "input.txt"


def main():
    with open(INPUT_FILE, "r") as reader:
        file_in = reader.read()
    elves = [map(int, el.split("\n")) for el in file_in.split("\n\n")]
    logger.debug(elves)

    elves_sums = [sum(elf) for elf in elves]
    max_elf = max(elves_sums)
    max_three_sum = sum(sorted(elves_sums)[-3:])

    logger.info(f"Max val: {max_elf}")
    logger.info(f"First three elves: {max_three_sum}")


if __name__ == "__main__":
    main()