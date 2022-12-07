#day6.py 2022
import unittest

def search(lines, offset):
    buffer = lines[0].strip()
    for i in range(len(buffer)-(offset-1)):
        s = set(buffer[i:i+offset])
        if len(s) == offset:
            return i+offset
    return None

def part1(lines):
    return search(lines, 4)

def part2(lines):
    return search(lines, 14)

class TestDay6(unittest.TestCase):
    def test_1a(self):
        with open('./test6a.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 7)

    def test_1b(self):
        with open('./test6b.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 5)

    def test_1c(self):
        with open('./test6c.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 6)

    def test_1d(self):
        with open('./test6d.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 10)

    def test_1e(self):
        with open('./test6e.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 11)

    def test_1(self):
        with open('./input6.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 1142)

    def test_2a(self):
        with open('./test6a.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 19)

    def test_2b(self):
        with open('./test6b.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 23)

    def test_2c(self):
        with open('./test6c.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 23)

    def test_2d(self):
        with open('./test6d.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 29)

    def test_2e(self):
        with open('./test6e.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 26)

    def test_2(self):
        with open('./input6.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 2803)

if __name__ == '__main__':
    unittest.main()
