class Tower:
    def __init__(self):
        self.count = 0
    
    
    def solve(self, n, src, dst, tmp):
        if n == 1:
            self.print_move(src, dst)
        else:
            self.solve(n-1, src, tmp, dst)
            self.solve(1, src, dst, tmp)
            self.solve(n-1, tmp, dst, src)
        return self.count
    
    
    def print_move(self, src, dst):
        #print("Moving from {s} to {d}".format(s=src, d=dst))
        self.count += 1
