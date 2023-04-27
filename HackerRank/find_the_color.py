import re

sector = r"#[0-9a-fA-F]{6}(?!\S)|#[0-9A-Fa-f]{3}(?!\S)"
pattern = r"#[0-9a-fA-F]{6}|#[0-9A-Fa-f]{3}"
#pattern = r"#[0-9a-fA-F]{6}(?=[;),])|#[0-9A-Fa-f]{3}(<=[;),])"
for _ in range(int(input())):
    string = input()
    name = re.findall(sector,string)
    color = re.findall(pattern, string)
    for code in color:
        if code not in name:
            print(code)
