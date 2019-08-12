class Hanoi:
    def __init__(self, file):
        n, moves = self.read_input(file)
        self.disks = n
        self.moves = moves

        if self.check_input() != "NO":
            disks = []
            for i in range(int(n)):
                disks.append(i)
            disks.reverse()
            self.disk_array = disks
            self.rods = {
                "1": disks,
                "2": [],
                "3": [] 
            }

    def read_input(self, file):
        try:
            with open(file, 'r') as f:
                text = f.read()
                lines = text.split('\n')
        except Exception as e:
            print(str(e))
        
        disks = lines[0]
        moves = lines[1:]
        
        return disks, moves

    def check_input(self):
        # Check disks is integer
        try:
            self.disks = int(self.disks)
        except ValueError as ve:
            print(str(ve))
            return "NO"

        # Check there is at least 1 disk at the begining
        if self.disks < 1:
            return "NO"
        
        # Make sure only 3 rods are involved (1,2,3) 
        for line in self.moves:
            if line not in ['12', '13', '21', '23', '31', '32']:
                print("Illegal input")
                return "NO"

    def move(self, i):
        origin = self.moves[i][0]
        destination = self.moves[i][1]

        # Check that the source rod is not empty  
        if not self.rods[origin]:
            print("Cannot retrieve disks from empty rod")
            return "NO"

        disk = self.rods[origin][-1]     # retrieved disk from source rod
        self.rods[origin].pop()

        # Validate that the disk in target rod is not smaller than the new disk inserted
        if self.rods[destination]:
            if self.rods[destination][-1] < disk:
                print("Move violates the rules.")
                return "NO"
            else:
                self.rods[destination].append(disk)
        else:
            self.rods[destination].append(disk)
        print(self.rods)
    
    def check_if_won(self):
        input_is_valid = self.check_input()
        if input_is_valid == "NO":
            return "NO"

        min_moves = 2 ** self.disks - 1 
        print(min_moves)
        if len(self.moves) < min_moves:
            print("At least", min_moves, "moves are required to solve this problem")
            return "NO"

        for i in range(len(self.moves)):
            move = self.move(i)
            if move == "NO":
                return "NO"

        # Check either rod 2 or 3 holds the all disks in the proper order
        print(self.disk_array)
        if self.rods["2"] == self.disk_array or self.rods["3"] == self.disk_array:
            return "YES"
        else:
            return "NO"
        


    
