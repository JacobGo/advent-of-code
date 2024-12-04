def peak(file, i = 1):
    c = file.read(i)
    if len(c) < i:
        return None
    file.seek(file.tell() - min((len(c), i)))
    return c

def read_int(file):
    num = ''
    while True:
        c = peak(file)
        if not c.isdigit():
            break
        num += file.read(1)

    return int(num)


def solve(part):
    file = open('3.in')
    sum = 0
    on = True
    while c := file.read(1):
        if c == 'd':
            if peak(file, 6) == "on't()":
                on = False
                file.read(6)
                continue
            if peak(file, 3) == 'o()':
                on = True
                file.read(3)
                continue

        if part == 2 and not on:
            continue

        if c != 'm':
            continue
        if file.read(1) != 'u':
            continue
        if file.read(1) != 'l':
            continue

        left = None
        if file.read(1) != '(':
            continue

        left = read_int(file)
        if not left:
            continue

        if file.read(1) != ',':
            continue

        right = read_int(file)
        if not right:
            continue

        if file.read(1) == ')':
            sum += left * right
    return sum

print("Part 1:", solve(1))
print("Part 2:", solve(2))
