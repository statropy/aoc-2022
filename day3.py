#day3.py 2022
import unittest

def priority(c):
    if c >= 'a' and c <= 'z':
        return ord(c)-ord('a')+1
    return ord(c)-ord('A')+27

def part1(lines):
    sump = 0
    for line in lines:
        line = line.strip()
        half = len(line) // 2
        for item in set(line[:half]).intersection(line[half:]):
            sump += priority(item)
    return sump

def part2(lines):
    sump = 0
    while lines:
        [a, b, c], lines = [l.strip() for l in lines[:3]], lines[3:]
        for item in set(a).intersection(b).intersection(c):
            sump += priority(item)
    return sump

class TestDay3(unittest.TestCase):
    def test_1a(self):
        with open('./test3.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 157)

    def test_1(self):
        with open('./input3.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 7701)

    def test_2a(self):
        with open('./test3.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 70)

    def test_2(self):
        with open('./input3.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 2644)

if __name__ == '__main__':
    unittest.main()
