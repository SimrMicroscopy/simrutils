import nd2reader
import numpy as np


import numpy as np
import tifffile
from nd2reader import ND2Reader
from matplotlib import pyplot as plt

class nikonImage():
    '''
    Class to read Nikon nd2 images
    '''    
    def __init__(self, filename):
        self.filename = filename
        self.nd2 = ND2Reader(filename)
        self.set_sizes(self.nd2.sizes)
    
    def set_sizes(self, sizes):
        
        if 't' not in sizes:
            sizes['t'] = 1
        if 'z' not in sizes:
            sizes['z'] = 1
        if 'c' not in sizes:
            sizes['c'] = 1
        self.sizes = sizes
        self.shape = (self.sizes['t'], self.sizes['z'], self.sizes['c'],
                    self.sizes['y'], self.sizes['x'])
        
        
    def __call__(self, squeeze=True):   
        self.nd2.bundle_axes = 'zcyx'
        self.nd2.iter_axes = 't'
        n = len(self.nd2.iter_axes)
        
        image  = np.zeros(self.shape, dtype=np.float32)

        for i in range(n):
            image[i] = self.nd2.get_frame(i)

        if squeeze:
            return image.squeeze()
        else:
            return image
        
    def getMetadata(self):
        return self.nd2.metadata
    
    def close(self):
        self.nd2.close()