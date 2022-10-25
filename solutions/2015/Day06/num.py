import numpy as np

a = np.zeros((10,10), dtype=int)
m = np.asmatrix(a)

print(m)
print(m.sum())

coord = [(1,1), (8,8)]
(x1,y1),(x2,y2) = coord
m[x1:x2+1, y1:y2+1] = 1

print(m)
print(m.sum())
