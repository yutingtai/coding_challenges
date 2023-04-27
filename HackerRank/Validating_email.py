import re

pattern = r"<[a-zA-Z][a-zA-Z0-9\.\_\-]+\@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
for _ in range(int(input())):
    name, email = list(map(str, input().split()))
    if bool(re.search(pattern, email)):
        print(name, email)

