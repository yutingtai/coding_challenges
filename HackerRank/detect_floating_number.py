import re


for _ in range(int(input())):
    print(True if re.search(r"^[+-]?\d*\.\d+$", input()) else False)
