"""
Util for generating tests with random values and 10000 step.
"""

import random

for count in [i for i in range(0, 1000001, 10000)]:
    with open(f"test_el_{count}.txt", "w", encoding="utf-8") as f:
        for _ in range(count):
            f.write(f"{random.randrange(-500, 500)} ")
        f.write("\n")
