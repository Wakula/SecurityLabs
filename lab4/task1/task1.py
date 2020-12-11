import random
from collections import defaultdict


# source: https://stackoverflow.com/questions/3540288/how-do-i-read-a-random-line-from-one-file
def get_random_line_from_file(file):
    line = next(file)
    for num, aline in enumerate(file, 2):
        if random.randrange(num):
            continue
        line = aline
    return line
d = defaultdict(int)
for _ in range(100):
    with open('most_common_1_000_000_passwords') as f:
        d[get_random_line_from_file(f)] += 1
print(d)