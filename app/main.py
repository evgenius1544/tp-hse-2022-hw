"""
Implement in Python a simple program that will read numbers from a file,
and then use separate functions to search among these numbers for the minimum number,
the maximum number, count their total sum and product.
"""

import sys
import os

from functools import reduce

from typing import Union
from typing import List


Number = Union[int, float]


def _min(values: List[Number]) -> Number:
    """
    _min
        Finds min element in sequence.

    Args:
        values (List[Number]): values.

    Returns:
        Number: minimum.
    """

    return min(values)


def _max(values: List[Number]) -> Number:
    """
    _max
        Finds max element in sequence.

    Args:
        values (List[Number]): values.

    Returns:
        Number: maximum.
    """

    return max(values)


def _sum(values: List[Number]) -> Number:
    """
    _sum
        Function sums new value with previous result.

    Args:
        values (List[Number]): values.

    Returns:
        Number: result of sum.
    """

    return sum(values)


def _mult(values: List[Number]) -> Number:
    """
    _mult
        Function multiples new value with previous result.

    Args:
        values (List[Number]): values.

    Returns:
        Number: result of mult.
    """

    return reduce(lambda x, y: x * y, values)


def _read(file_path: str) -> List[Number]:
    """
    _read
        Reads all values from file.


    Returns:
        List[Number]: values in list.
    """

    with open(file_path, mode="r", encoding="utf-8") as file:
        return [float(el) for el in file.readline().split()]


def _output(min_: Number, max_: Number, sum_: Number, mult_: Number) -> None:
    """
    _output
        Outputs data.
    """

    print(min_, max_, sum_, mult_)


def main(file_name: str, output: bool = False) -> None:
    """
    main
        Reads values and processes them.
    """

    if not os.path.exists(file_name):
        exit("Args error: File not found ...")

    file_path = os.path.abspath(file_name)

    values = _read(file_path)

    minimum = _min(values)
    maximum = _max(values)
    summa = _sum(values)
    multiplication = _mult(values)

    if output:
        _output(minimum, maximum, summa, multiplication)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        exit("Args error: Waiting your file ...")

    main(sys.argv[1], output=True)
