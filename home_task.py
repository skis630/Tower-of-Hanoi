def read_input(file):
    text = ""
    lines = []
    try:
        with open(file, 'r') as f:
            text = f.read()
            lines = text.split('\n')
            print(lines)
    except Exception as e:
        return print(str(e))

    disks = ""
    moves = ""
    try:
        disks = int(lines[0])
    except ValueError as ve:
        print("NO")
        return print(str(ve))

    moves = lines[1:]
    for line in moves:
        if line not in ['12', '13', '21', '23', '31', '32']:
            print("Illegal input")
            return print("NO")    
    return has_won(disks, moves)


def has_won(n, moves):
    min_moves = 2 ** n - 1 
    print(min_moves)
    if len(moves) < min_moves:
        print("test1")
        print("At least", min_moves, "moves are required to solve this problem")
        return print("NO")

    
    disks = []
    for i in range(n):
        disks.append(i)
    disks.reverse()

    rods = {
        "1": disks,
        "2": [],
        "3": []
    }
    print(rods)

    for move in moves:
        origin = move[0]
        destination = move[1]

        # Check that the source rod is not empty  
        if not rods[origin]:
            print("test2")
            print("Cannot retrieve disks from empty rod")
            return print("NO")

        disk = rods[origin][-1]     # retrieved disk from source rod
        rods[origin].pop()

        # Validate that the disk in target rod is not smaller than the new disk inserted
        if rods[destination]:
            if rods[destination][-1] < disk:
                print("test3")
                print(rods)
                print("Move violates the rules.")
                return print("NO")
            else:
                rods[destination].append(disk)
        else:
            rods[destination].append(disk)
    
    print(rods)
    # Check either rod 2 or 3 holds the all disks in the proper order
    if rods["2"] == disks or rods["3"] == disks:
        print("test4")
        print("YES")
        return "YES"
    else:
        return print("NO")


if __name__ == "__main__":
    read_input("input9.txt")


