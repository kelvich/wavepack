from matplotlib import pyplot

class Graph:

    def __init__(self):
        self.plt = pyplot

    def push(self,data):
        self.plt.plot(data[0],data[1])
    
    def show(self):    
        self.plt.gca().set_yscale('log')
        self.plt.grid(True)
        self.plt.show()
