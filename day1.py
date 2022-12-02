#day1.py 2022
import unittest

def get_sums(lines):
    sums = [0]
    for s in lines:
        if s == '\n':
            sums.append(0)
        else:
            sums[-1] += int(s.strip())
    return sums

def get_sums_comp(lines):
    lines = [s.strip()+',' if s != '\n' else ';' for s in lines]
    groups = ''.join(lines).split(';')
    return [sum([int(s) for s in g.split(',') if len(s) > 0]) for g in groups]

def get_sums_orig(lines):
    lines.append('\n')
    elves = []
    while lines:
        for i,item in enumerate(lines):
            if item == '\n':
                elves.append([int(s.strip()) for s in lines[:i]])
                lines = lines[i+1:]
                break
    return [sum(cals) for cals in elves]

def part1(lines):
    return max(get_sums(lines))

def part2(lines):
    sums = sorted(get_sums(lines))
    return sum(sums[-3:])

class TestDay1(unittest.TestCase):
    def test_1a(self):
        with open('./test1.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 24000)
            # self.assertEqual(part1([item.strip() for item in f]), None)

    def test_1(self):
        with open('./input1.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 64929)

    def test_2a(self):
        with open('./test1.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 45000)

    def test_2(self):
        with open('./input1.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 193697)

if __name__ == '__main__':
    unittest.main()
