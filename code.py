import tkinter

presavesMaps = { "simple": [[0,1,1,1],
                             [3,1,1,4],
                              [2,1,1,0],
                               [0,0,0,0]]} # for tests

class Map:
    def clear(self, size):
        empty_map = []
        for i in range(size):
            line = []
            for j in range(size):
                line.append(0)
            empty_map.append(line)
        self.map = empty_map
    def set(self, map):
        self.map = map
    def display(self):
        print(self.map)
    def get_n(self, y, x): # temp (neighbours, possibles neighbours, possible x, possible y)
        ns = []
        pns = [(y-1,x), (y-1,x+1), (y,x-1), (y,x+1), (y+1,x-1), (y+1,x)]
        for py,px in pns:
            if self.map[py][px] != 0 and py in range(0, len(self.map)) and px in range(0, len(self.map)):
                ns.append(self.map[py][px])
        return ns

map = Map()
map.set(presavesMaps["simple"])
map.display()
print("voisins de '3': " + str(map.get_n(1,0)))
