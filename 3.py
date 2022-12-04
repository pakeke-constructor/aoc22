

prios = "abcdefghijklmnopqrstuvwxyz"
prios += prios.upper()

prio_map = {}

for i,c in enumerate(prios):
    prio_map[c] = i+1


def prio(x: str):
    return prio_map[x]

total_points = 0


def part1(rucksack):
    global total_points
    l2 = len(rucksack)//2
    left = rucksack[:l2]
    right = set(rucksack[l2:])
    for c in left:
        if c in right:
            total_points += prio(c)
            break

def part2(buf,i):
    global total_points
    x = set(buf[i])
    y = set(buf[i+1])
    z = set(buf[i+2])
    un = x.intersection(y).intersection(z)
    val = un.pop()
    total_points += prio(val)

with open("input") as f:
    buf = list(f.readlines())
    buf = list(map(lambda x: x.replace("\n",""), buf))
    for i in range(0, len(buf), 3):
        # part1(buf[i])
        part2(buf,i)

print(total_points)
