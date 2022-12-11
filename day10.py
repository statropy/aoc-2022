#day10.py 2022
import unittest

def part1(lines):
    x = 1
    cycle = 1
    v = None
    strengths = []
    i = len(lines)
    while i>0:
        p = cycle - 1
        ss = cycle * x
        if cycle >= 20 and (cycle + 20) % 40 == 0:
            strengths.append(ss)
            # print(cycle, ss)

        if v is None:
            cmd = lines.pop(0)
            i = len(lines)
            if cmd == 'noop\n':
                pass
            else:
                inst, v = cmd.strip().split(' ')
        else:
            x += int(v)
            v = None

        cycle += 1

    return sum(strengths)

def part2(lines):
    x = 1
    cycle = 1
    v = None
    crt = ''

    print()
    
    i = len(lines)
    while i>0:
        p = (cycle - 1) % 40
        c = ' '
        if p in [x-1, x, x+1]:
            c = '\u2588'
        crt += c

        if cycle % 40 == 0:
            print(crt)
            crt = ''

        if v is None:
            cmd = lines.pop(0)
            i = len(lines)
            if cmd == 'noop\n':
                pass
            else:
                inst, v = cmd.strip().split(' ')
        else:
            x += int(v)
            v = None

        cycle += 1

    return None

class TestDay10(unittest.TestCase):
    def test_1a(self):
        with open('./test10.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 13140)

    def test_1(self):
        with open('./input10.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 12640)

    def test_2a(self):
        with open('./test10.txt', 'r') as f:
            self.assertEqual(part2(list(f)), None)

    def test_2(self):
        with open('./input10.txt', 'r') as f:
            self.assertEqual(part2(list(f)), None)

if __name__ == '__main__':
    unittest.main()
