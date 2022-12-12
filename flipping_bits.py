#!/bin/python3

import math
import unittest


def flipping_bits(n):
    bits = decimal_to_bits(n)
    print(f"decimal {n} in binary is {bits}")
    flipped_bits = flip_bits(bits)
    decimal = bits_to_decimal(flipped_bits)
    print(f"binary {flipped_bits} in decimal is {decimal}")


def decimal_to_bits(n):
    q = n
    bits = 32 * [0]
    index = 31
    while q > 0:
        k = q % 2
        q = math.floor(q / 2)
        bits[index] = k
        index-=1
    return bits


def bits_to_decimal(bits):
    decimal = 0
    for i in range(len(bits) - 1, -1, -1):
        k = len(bits) - 1 - i
        decimal += int(math.pow(2, i)) * bits[k]
    return decimal


def flip_bits(b):
    flipped = 32 * [0]
    for i in range(0, len(b)):
        if b[i] == 0:
            flipped[i] = 1
        else:
            flipped[i] = 0
    print(f"flipped = {flipped}")
    return flipped


class TestFlippingBits(unittest.TestCase):

    def test_bits_to_decimal(self):
        self.assertEqual(0, bits_to_decimal([0]))
        self.assertEqual(0, bits_to_decimal([0, 0]))
        self.assertEqual(0, bits_to_decimal([0, 0, 0]))
        self.assertEqual(1, bits_to_decimal([1]))
        self.assertEqual(2, bits_to_decimal([1, 0]))
        self.assertEqual(3, bits_to_decimal([1, 1]))
        self.assertEqual(5, bits_to_decimal([1, 0, 1]))
        self.assertEqual(7, bits_to_decimal([1, 1, 1]))
        self.assertEqual(10, bits_to_decimal([1, 0, 1, 0]))
        self.assertEqual(21, bits_to_decimal([1, 0, 1, 0, 1]))
