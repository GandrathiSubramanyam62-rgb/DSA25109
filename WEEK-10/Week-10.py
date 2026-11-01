#G.Subramanyam
SIZE = 11
# 1. Separate Chaining
def separate_chaining(keys):
    table = [[] for _ in range(SIZE)]
    for key in keys:
        index = key % SIZE
        table[index].append(key)
    print("\nSeparate Chaining:")
    for i in range(SIZE):
        print(i, ":", table[i])
# 2. Linear Probing
def linear_probing(keys):
    table = [None] * SIZE
    for key in keys:
        index = key % SIZE
        for i in range(SIZE):
            pos = (index + i) % SIZE
            if table[pos] is None:
                table[pos] = key
                break
        else:
            print("Table is full. Cannot insert:", key)
    print("\nLinear Probing:")
    for i in range(SIZE):
        print(i, ":", table[i])
# 3. Quadratic Probing
def quadratic_probing(keys):
    table = [None] * SIZE
    for key in keys:
        index = key % SIZE
        for i in range(SIZE):
            pos = (index + i * i) % SIZE
            if table[pos] is None:
                table[pos] = key
                break
        else:
            print("Cannot insert:", key)
    print("\nQuadratic Probing:")
    for i in range(SIZE):
        print(i, ":", table[i])
# Main Program
keys = list(map(int, input("Enter keys: ").split()))

separate_chaining(keys)
linear_probing(keys)
quadratic_probing(keys)
