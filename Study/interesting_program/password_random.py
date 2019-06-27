x=int(input())
choices="1234567890"
for small in list(map(chr, range(ord('a'), ord('z') + 1))):
    choices+=small
for big in list(map(chr, range(ord('A'), ord('Z') + 1))):
    choices+=big
print(''.join(__import__('random').choice(choices) for i in range(x)))
