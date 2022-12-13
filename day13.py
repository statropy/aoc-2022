#day13.py 2022
import unittest
import functools

def compare(left, right):
    tl, tr = type(left), type(right)
    if tl == int and tr == int:
        if left < right:
            return -1
        if right < left:
            return 1
        return None
    if tl == int:
        left = [left]
    elif tr == int:
        right = [right]

    for i in range(min([len(left), len(right)])):
        v = compare(left[i], right[i])
        if v is not None:
            return v
    if len(left) < len(right):
        return -1
    if len(right) < len(left):
        return 1
    return None

def part1(lines):
    pairing = 0
    valid = []
    while(len(lines) > 0):
        if len(lines[0]) == 1:
            lines.pop(0)
        pairing += 1
        left = eval(lines.pop(0).strip())
        right = eval(lines.pop(0).strip())
        if compare(left, right) < 0:
            valid.append(pairing)
    return sum(valid)

def part2(lines):
    rows = [eval(r.strip()) for r in lines if r != '\n']
    two = eval('[[2]]')
    six = eval('[[6]]')
    rows.append(two)
    rows.append(six)
    s = sorted(rows, key=functools.cmp_to_key(compare))
    return (s.index(two)+1) * (s.index(six)+1)

class TestDay13(unittest.TestCase):
    def test_1a(self):
        with open('./test13.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 13)

    def test_1a_1(self):
        self.assertEqual(compare([1,1,3,1,1],[1,1,5,1,1]),-1)

    def test_1a_2(self):
        self.assertEqual(compare([[1],[2,3,4]],[[1],4]),-1)

    def test_1a_3(self):
        self.assertEqual(compare([9],[[8,7,6]]),1)

    def test_1a_4(self):
        self.assertEqual(compare([[4,4],4,4],[[4,4],4,4,4]),-1)

    def test_1a_5(self):
        self.assertEqual(compare([7,7,7,7],[7,7,7]),1)

    def test_1a_6(self):
        self.assertEqual(compare([],[3]),-1)

    def test_1a_7(self):
        self.assertEqual(compare([[[]]],[[]]),1)

    def test_1a_8(self):
        self.assertEqual(compare([1,[2,[3,[4,[5,6,7]]]],8,9],[1,[2,[3,[4,[5,6,0]]]],8,9]),1)

    def test_1(self):
        with open('./input13.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 5843)

    def test_2a(self):
        with open('./test13.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 140)

    def test_2(self):
        with open('./input13.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 26289)

if __name__ == '__main__':
    unittest.main()
