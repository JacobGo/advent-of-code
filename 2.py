file = open("2.in")


def check(first, next, is_asc):
    diff = abs(first - next)
    if diff > 3 or diff < 1:
        return False

    if is_asc:
        if first > next:
            return False
    else:
        if first < next:
            return False
    return True

def attempt(levels):
    i = 1
    is_asc = levels[0] < levels[1]

    while i < len(levels):
        first = levels[i-1]
        next = levels[i]
        i += 1

        if not check(first, next, is_asc):
          return False

    return True

safe_reports = 0
safe_reports_with_check = 0
for line in file.readlines():
    levels = [int(c) for c in line.split()]

    if attempt(levels):
        safe_reports += 1
  
    is_safe = False
    for [i, _] in enumerate(levels):
        levels2 = list(levels)
        del levels2[i]
        if attempt(levels2):
            is_safe = True

    if is_safe:
        safe_reports_with_check += 1

    # gen permutations
        
print("Part 1:", safe_reports)
print("Part 2:", safe_reports_with_check)