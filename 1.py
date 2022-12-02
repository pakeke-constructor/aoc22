

elfs = []

with open("input") as f:
    buf = []
    for x in f.readlines():
        x = x.replace("\n","")
        if not x and buf:
            elfs.append(sum(buf))
            buf = []
        else:
            buf.append(int(x))


elfs.sort()

print(elfs[-1] + elfs[-2] + elfs[-3])
