
import pickle
import numpy as np

filename = 'model1.h5'
infile = open(filename,'rb')
model = pickle.load(infile)
infile.close()



#model.score()
arr =  np.array([[1,2,3,3,3,5,1]])
arr.reshape(-1,1)
print(model.columns)

print(model.predict(arr))




'''with h5py.File(filename, 'r') as f:
    # List all groups
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]

    # Get the data
    data = list(f[a_group_key])'''
