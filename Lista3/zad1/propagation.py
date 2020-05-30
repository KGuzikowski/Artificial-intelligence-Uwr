import numpy as np
import itertools
import random
from functools import lru_cache


class Nonogram():

    def __init__(self, rows, cols, row_desc, col_desc):
        self.r = rows                # Number of rows
        self.c = cols                # Number of cols
        self.row_desc = row_desc     # Rows description
        self.col_desc = col_desc     # Cols description

        self.nono = np.zeros((rows, cols), dtype=np.int8)    # A board matrix

        # A set of rows (cols) domain
        self.rowDomain, self.colDomain = self.getDomains()
        self.isTransposed = False

    def __str__(self):
        return '\n'.join([''.join(["#" if v == 1 else "." for v in row])
                         for row in (self.nono if self.isTransposed is False
                                     else self.nono.T)])

    def __repr__(self):
        return self.__str__()

    def info(self):
        print("{} x {}".format(self.r, self.c))
        print("Rows desc: {}".format(self.row_desc))
        print("Cols desc: {}".format(self.col_desc))

    def transpose(self):
        self.r, self.c = self.c, self.r
        self.rowDomain, self.colDomain = self.colDomain, self.rowDomain
        self.nono = self.nono.transpose()
        self.isTransposed = not self.isTransposed

    def getDomain(self, row_desc, row_len):
        row_desc = list(row_desc)

        if len(row_desc) == 1:
            zeros = row_len - row_desc[0]
            return {tuple([0]*i + [1]*row_desc[0] + [0]*(zeros-i))
                    for i in range(zeros + 1)}

        limit = row_len - row_desc[-1]
        ans = []
        for comb in itertools.combinations(range(limit + 1), len(row_desc)):
            not_overlapping = True
            for c in range(len(comb) - 1):
                if comb[c] + row_desc[c] >= comb[c+1]:
                    not_overlapping = False
                    break
            if not_overlapping:
                t = [0] * row_len
                for i, c in enumerate(comb):
                    for j in range(c, c + row_desc[i]):
                        t[j] = 1
                ans.append(t)

        return {tuple(a) for a in ans}

    def getDomains(self):
        return ([self.getDomain(row, self.c) for row in self.row_desc],
                [self.getDomain(col, self.r) for col in self.col_desc])

    def intersectDomain(self, dom, what=1):
        dom = list(dom)
        intersect = list(dom[0])
        for i in range(1, len(dom)):
            intersect = [what if a == b and b == what else 1-what
                         for a, b in zip(intersect, dom[i])]
        return intersect

    def isSolved(self):
        for i, row in enumerate(self.nono):
            if tuple(row) not in self.rowDomain[i]:
                return False

        for j, col in enumerate(self.nono.T):
            if tuple(col) not in self.colDomain[j]:
                return False
        return True

    def constrainDomain(self, pixels, what):
        for i, j in pixels:
            toRemove = []
            for col in self.colDomain[j]:
                if col[i] == what:
                    toRemove.append(col)
            for rm in toRemove:
                self.colDomain[j] -= {rm}

    def ac3(self):
        while self.isSolved() is False:
            pixelsToBeOn = set()
            pixelsToBeOff = set()

            for i, row in enumerate(self.rowDomain):
                for j, r in enumerate(self.intersectDomain(row)):
                    if r == 1:
                        self.nono[i][j] = 1
                        pixelsToBeOn |= {(i, j)}

                for j, r in enumerate(self.intersectDomain(row, what=0)):
                    if r == 0:
                        self.nono[i][j] = 0
                        pixelsToBeOff |= {(i, j)}

            self.constrainDomain(pixelsToBeOn, what=0)
            self.constrainDomain(pixelsToBeOff, what=1)

            self.transpose()


def readFromFile(finput):
    lines = []
    with open(finput) as f:
        for line in f:
            lines.append(list(map(int, line.strip('\n').split())))
    r, c = lines[0][0], lines[0][1]

    return Nonogram(r, c, row_desc=lines[1:r+1], col_desc=lines[r+1:])


finput = 'zad_input.txt'
foutput = 'zad_output.txt'

nono = readFromFile(finput)

nono.ac3()
print(nono)

fout = open(foutput, "w")
print(nono, file=fout)