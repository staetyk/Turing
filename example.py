from turing import Turing


print("Binary Incrementor:\n")
increment = Turing(
    ((0, 0, True), (0, 1, True), (1, -1, False)),
    ((2, 1, False), (1, 0, False), (2, 1, True)),
    ((2, 0, True), (2, 1, True), (-1, -1, False)),
    tape = input(), shorten = True)
x = increment.copy()
while True:
    print(x)
    if x: break
    else: x()
