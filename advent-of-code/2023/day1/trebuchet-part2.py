from collections import OrderedDict
import re

from pprint import PrettyPrinter
pp = PrettyPrinter(2, 1)



"""
===================================================
In this example, the calibration values are:
29, 83, 13, 24, 42, 14, and 76. 
Adding these together produces 281.


answer = ?
===================================================
"""



NUM_ALPHA: dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

NUM_ALPHA: dict = OrderedDict(NUM_ALPHA)



def get_file_data() -> dict:
    with open(file="part2-sample-input",
              mode="r",
              encoding="utf-8") as file:
        return {key: value.strip() for key, value in enumerate(file)}




def main() -> None:
    input_file: dict = get_file_data()

    for line in input_file.values():
        for char in line:
            pass


    print(f"\n***In The End***\n")



if __name__ == "__main__":
    main()


