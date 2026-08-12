import re

n = int(input())


pattern = r'(?<=.)#(?:[a-fA-F0-9]{6}|[a-fA-F0-9]{3})\b'

for _ in range(n):
    line = input()
    matches = re.findall(pattern, line)
    for match in matches:
        print(match)