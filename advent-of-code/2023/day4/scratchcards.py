from dataclasses import (
    dataclass,
    field,
)
import sys
import re

import pprint
pp = pprint.PrettyPrinter(indent=2, width=1)


@dataclass
class Card:
    card_id: int = field()

    winning_numbers: list = field(default_factory=list)
    numbers_to_match: list = field(default_factory=list)

    number_of_matches: int = field(default=0)


def get_numbers_to_match(data: str) -> list:
    to_match_side: list = data.split(sep="|", maxsplit=1)
    to_match_numbers: list = re.findall(pattern=r"(\d+)", string=to_match_side[1])

    return to_match_numbers


def get_winning_nums(data: str) -> list:
    win_side: list = data.split(sep="|", maxsplit=1)
    win_nums: list = re.findall(pattern=r"(\d+)", string=win_side[0])

    return win_nums


def get_card_id(data: str) -> int:
    card_id: int = int(
        re
        .search(pattern=r"\w+ (\d+)", string=data)
        .group(1)
    )

    return card_id


def get_input_data() -> list:
    with open(file="part1-sample-input",
              mode="r",
              encoding="utf-8") as file:
        all_cards: list[Card] = []

        for line_data in file:
            data: str = line_data.strip()

            card_section = data.split(sep=":", maxsplit=1)

            card_id: int = get_card_id(data=card_section[0])
            win_nums: list = get_winning_nums(data=card_section[1])
            nums: list = get_numbers_to_match(data=card_section[1])

            all_cards.append(
                Card(card_id=card_id,
                     winning_numbers=win_nums,
                     numbers_to_match=nums)
            )

        file.close()
        del file

        return all_cards


def main() -> None:
    card_data: list[Card] = get_input_data()

    print(f"\n\n***THE END***\n\n")
    sys.exit(1)


if __name__ == "__main__":
    main()

