from tkinter import *

presavesMaps = { "simple": [[0,0,2,1,0],
                             [0,3,2,2,1],
                              [2,2,1,2,2],
                               [2,1,2,4,1],
                                [2,2,1,0,0]]} # for tests

class Map:
    def clear(self, size):
        empty_map = []
        for i in range(size):
            y = []
            for j in range(size):
                y.append(0)
            empty_map.append(y)
        self.map = empty_map
    def set(self, map):
        self.map = map
    def display(self):
        fen = Tk()
        grille = Canvas(fen, width=700, height=500, background='white')
        size = int(500/(len(self.map)+1))
        for y in range (1, len(self.map)+1):
            for x in range (len(self.map)):
                decalage = (y * 0.55 +  x * 0.1) * size
                hexagone = [(x)       * size + decalage, (y - 0.6) * size,
                            (x + 0.5) * size + decalage, (y - 0.3) * size,
                            (x + 0.5) * size + decalage, (y + 0.3) * size,
                            (x)       * size + decalage, (y + 0.6) * size,
                            (x - 0.5) * size + decalage, (y + 0.3) * size,
                            (x - 0.5) * size + decalage, (y - 0.3) * size]
                rond = [(x-0.2) * size + decalage, (y-0.2) * size,
                        (x+0.2) * size + decalage, (y+0.2) * size,]
                if self.map[y - 1][x] == 1:
                    grille.create_polygon(hexagone, fill = 'black')
                elif self.map[y - 1][x] >= 2:
                    grille.create_polygon(hexagone, fill='grey')
                if self.map[y - 1][x] == 3:
                    grille.create_oval(rond, fill='red')
                if self.map[y - 1][x] == 4:
                    grille.create_oval(rond, fill='blue')
        grille.pack()
        fen.mainloop()
    def get_n(self, y, x): # temp (neighbours, possibles neighbours, possible x, possible y)
        ns = []
        pns = [(y-1,x), (y-1,x+1), (y,x-1), (y,x+1), (y+1,x-1), (y+1,x)]
        for py,px in pns:
            if self.map[py][px] != 0 and py in range(0, len(self.map)) and px in range(0, len(self.map)):
                ns.append(self.map[py][px])
        return ns

map = Map()
map.set(presavesMaps["simple"])
print("voisins de '3': " + str(map.get_n(1,0)))
map.display()
