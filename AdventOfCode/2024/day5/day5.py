from collections import defaultdict
from typing import Tuple

# '29': {'13', '26'}  ====> 29一定要在 13, 26 之前


class Printer:
    def __init__(self, data):
        self.policy = defaultdict(set)
        self.data = data

    def __add_to_policy(self, line: str):
        first_appear, later_appear = line.split("|")
        self.policy[first_appear].add(later_appear)

    def __get_correct_middle_el(self, line: str) -> Tuple[bool, str | None]:
        pages = line.split(",")

        i = 0
        middle_el_index = len(pages) // 2 if len(pages) % 2 else int(len(pages) / 2)
        middle_el = None
        for i, page in enumerate(pages):
            remaining_pages = pages[i + 1 :]
            if self.policy[page]:
                for next_page in remaining_pages:
                    if next_page not in self.policy[page]:
                        return False, None
            if i == len(pages) - 1:
                remaining_pages = pages[:i]
                for next_page in remaining_pages:
                    if next_page in self.policy[page]:
                        return False, None

        middle_el = pages[middle_el_index]
        print("for sum up ==========> ", middle_el)
        return True, middle_el

    def get_correct_sum(self):
        total = 0
        for line in file:
            if "|" in line:
                self.__add_to_policy(line.strip())
            elif "," in line:
                print("target list: ", line.strip())
                correct, el = self.__get_correct_middle_el(line.strip())
                if correct and el:
                    total += int(el)

        return total

    def __get_incorrect_middle_el(self, line: str):
        pass

    def get_incorrect_sum(self):
        pass


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        p = Printer(file)
        s = p.get_correct_sum()
        print(s)
