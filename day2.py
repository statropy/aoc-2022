#day2.py 2022
import unittest

points = {'A':1, 'B':2, 'C':3, 'W':6, 'T':3, 'L':0}

choice1 = {'X':'A', 'Y':'B', 'Z':'C'}
choice2 = {'X':'L', 'Y':'T', 'Z':'W'}

outcome = {
    'A':{'A':'T','B':'L','C':'W'},
    'B':{'A':'W','B':'T','C':'L'},
    'C':{'A':'L','B':'W','C':'T'},
    'W':{'A':'B','B':'C','C':'A'},
    'L':{'A':'C','B':'A','C':'B'},
    'T':{'A':'A','B':'B','C':'C'},
}

def play(lines, choice):
    score = 0
    for line in lines:
        opponent, me = line.strip().split(' ')
        me = choice[me]
        rscore = points[me] + points[outcome[me][opponent]]
        score += rscore
    return score

def part1(lines):
    return play(lines, choice1)

def part2(lines):
    return play(lines, choice2)

class TestDay2(unittest.TestCase):
    def test_1a(self):
        with open('./test2.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 15)

    def test_1(self):
        with open('./input2.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 12458)

    def test_2a(self):
        with open('./test2.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 12)

    def test_2(self):
        with open('./input2.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 12683)

if __name__ == '__main__':
    unittest.main()
