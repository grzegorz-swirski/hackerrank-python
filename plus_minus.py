#!/bin/python3
import decimal
import unittest
from decimal import Decimal


# calculate ratios positive, negative, zero
def plus_minus(arr):
    positive = 0
    negative = 0
    zeroes = 0
    n = len(arr)
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zeroes += 1

    print(f"{Decimal(positive) / Decimal(n):.6f}")
    print(f"{Decimal(negative) / Decimal(n):.6f}")
    print(f"{Decimal(zeroes) / Decimal(n):.6f}")


if __name__ == '__main__':
    unittest.main()


class TestPlusMinus(unittest.TestCase):

    def test_plus_minus(self):
        arr = [1, 1, 0, -1, -1]
        plus_minus(arr)
