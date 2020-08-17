import numpy as np

from  simr_io.nd2read import nikonImage

def test_nikonImage():
    filename = '/Volumes/Samsung_T5/Quarantine/ND2/16 hours punched today-2001.nd2'
    nd2 = nikonImage(filename)
    image = nd2()
    print(nd2.sizes)
    print(image.shape)
    
    for k, v in nd2.getMetadata().items():
        print(k, v)
    
if __name__ == '__main__':
    test_nikonImage()