
import pickle


filename = 'model1.h5'
infile = open(filename,'rb')
model = pickle.load(infile)
infile.close()



print(model)

print(type(model))




'''with h5py.File(filename, 'r') as f:
    # List all groups
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]

    # Get the data
    data = list(f[a_group_key])'''
