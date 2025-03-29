import itertools


cheeses = input().split()
cheeses.pop(0)

stacks = []

for n in range(1, len(cheeses) + 1):
    perms = itertools.permutations(cheeses, r=n)

    new = []
    for stack in perms:
        new.append(tuple(sorted(stack, key=len)))

    perms = list(set(new))

    for stack in perms:
        if stack not in stacks:
            stacks.append(stack)

print(len(stacks))
