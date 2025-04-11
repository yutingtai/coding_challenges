import re


PATTERN = r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))"


total = 0
result = []
with open("input.txt") as f:
    for line in f:
        matches = re.findall(PATTERN, line)
        for match in matches:
            if match[0]:  # It's an 'aaa(X,Y)' match (entire match is in group 0)
                result.append(("mul", match[1], match[2]))  # (type, X, Y)
            elif match[3]:  # It's a 'do()' match (group 3 will contain the match)
                result.append(("do"))  # Mark it as 'do' with ("", "")
            elif match[4]:  # It's a 'don't()' match (group 4 will contain the match)
                result.append(("don't"))
                #  # Mark it as 'don't' with ("", "")


add_up = True
for val in result:
    if val == "do":
        add_up = True
    elif val == "don't":
        add_up = False
    else:
        if add_up:
            total += int(val[1]) * int(val[2])

print(total)
