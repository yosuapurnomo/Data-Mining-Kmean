import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class kmean:

    def __init__(self, data):
        self.data = data
        self.averageValue = None
        self.k = None

    def setkelas(self, k):
        self.k = k
        self.data['kelas'] = [random.randint(1, k) for _ in range(len(self.data))]

    def average(self):
        header = self.data.columns.values
        self.averageValue = [[self.data[x][self.data['kelas'] == k].mean() for x in header[:-1]] for k in range(1, self.k+1)]
        print(self.averageValue)
        for i in range(len(self.averageValue)):
            self.data[f'kelas{i+1}'] = np.sum([abs((self.data[header[x]] - self.averageValue[i][x])) for x in range(len(header[:-1]))])
        print(self.data)

    def mainLoop(self):
        while True:
            self.iterasi += 1
            target = self.data['kelas'].copy()
            # self.average()

data = pd.read_excel('dataset.xlsx', header=0)
Kmean = kmean(data)
Kmean.setkelas(3)
Kmean.average()