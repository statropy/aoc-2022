#day15.py 2022
import unittest

def part1(lines, row):
    empty = set()
    occupied = set()
    for line in lines:
        pairs = line.strip().replace('Sensor at ', '').replace(' closest beacon is at ','').replace('x=','').replace('y=','').split(':')
        sensor = tuple([int(z) for z in pairs[0].split(', ')])
        beacon = tuple([int(z) for z in pairs[1].split(', ')])

        if beacon[1] == row:
            occupied.add(beacon[0])
        d = abs(sensor[0]-beacon[0])+abs(sensor[1]-beacon[1])
        distance_to_row = abs(sensor[1]-row)
        if d >= distance_to_row:
            delta = d - distance_to_row
            toadd = list(range(sensor[0]-delta, sensor[0]+delta+1))
            empty.update(toadd)
    
    return len(empty.difference(occupied))

def add_ranges(a, b):
    if b[1] < a[0]-1 or b[0] > a[1]+1:
        return None
    return min(a[0], b[0]), max(a[1], b[1])

def condense(segments, s):
    retry = True
    while retry:
        retry = False
        updated = []
        for i,seg in enumerate(segments):
            combined = add_ranges(seg, s)
            if combined is None:
                updated.append(seg)
            else:
                retry = True
                s = combined
                if i < len(segments)-1:
                    updated += segments[i+1:]
                    break
        segments = updated
    segments.append(s)
    return segments

def part2(lines, limit=4000000):
    pairings = []
    skip = set()
    for line in lines:
        pairs = line.strip().replace('Sensor at ', '').replace(' closest beacon is at ','').replace('x=','').replace('y=','').split(':')
        sensor = tuple([int(z) for z in pairs[0].split(', ')])
        beacon = tuple([int(z) for z in pairs[1].split(', ')])
        pairings.append((sensor, beacon))
        if beacon[0] >= 0 and beacon[0] <= limit and beacon[1] >=0 and beacon[1] <= limit:
            skip.add(beacon[1])

    for row in range(limit+1):
        if row in skip:
            continue

        segments = []
        for sensor, beacon in pairings:
            d = abs(sensor[0]-beacon[0])+abs(sensor[1]-beacon[1])
            distance_to_row = abs(sensor[1]-row)
        
            if d >= distance_to_row:
                delta = d - distance_to_row
                s = (max(0,sensor[0]-delta),  min(limit,sensor[0]+delta))
                segments = condense(segments, s)
                if len(segments) == 1 and segments[0][0] == 0 and segments[0][1] == limit:
                    segments = []
                    break

        if len(segments) == 0:
            continue
        if len(segments) == 1:
            if segments[0][0] == 0:
                return limit * limit + row
            else:
                return row
        elif len(segments) == 2:
            segments.sort()
            return (segments[0][1]+1) * limit + row

class TestDay15(unittest.TestCase):
    def test_1a(self):
        with open('./test15.txt', 'r') as f:
            self.assertEqual(part1(list(f),10), 26)

    def test_1(self):
        with open('./input15.txt', 'r') as f:
            self.assertEqual(part1(list(f),2000000), 5525990)

    def test_2a(self):
        with open('./test15.txt', 'r') as f:
            self.assertEqual(part2(list(f), 20), 291) #56000011

    def test_2(self):
        with open('./input15.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 11756174628223)

if __name__ == '__main__':
    unittest.main()
