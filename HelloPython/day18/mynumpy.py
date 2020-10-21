import numpy as np

data = np.load('x_train.npy')
print(data)


for i in data:
    print('==========================================================================================')
    for j in i:
        for k in range(len(j)):
            if(j[k] > 0):
                j[k] = 1
            else:
                j[k] = 0
        print(j)