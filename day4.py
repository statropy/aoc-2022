#day4.py 2022
import unittest

def splitrange(r):
    start, end = [int(x) for x in r.split('-')]
    return set(range(start, end+1))

def parse_orig(lines):
    return [[splitrange(r) for r in line.strip().split(',')] for line in lines]

def parse(lines, condition):
    return len([(a,b) for a, b in [[ set(range(*[sum(z) for z in zip([0,1],[int(x) for x in r.split('-')]) ])) for r in line.strip().split(',')] for line in lines] if condition(a,b)])

def part1(lines):
    return parse(lines, lambda a,b: a.issubset(b) or b.issubset(a))

def part2(lines):
    return parse(lines, lambda a,b: len(a.intersection(b)) > 0)

class TestDay4(unittest.TestCase):
    def test_1a(self):
        with open('./test4.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 2)

    def test_1(self):
        with open('./input4.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 431)

    def test_2a(self):
        with open('./test4.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 4)

    def test_2(self):
        with open('./input4.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 823)

if __name__ == '__main__':
    unittest.main()
