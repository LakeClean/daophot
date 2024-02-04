#Correcting fits_data for daophot:
from astropy.io import fits
import numpy as np
import glob
import os
import sys


directory = sys.argv[1]

if len(directory) < 1:
    if 'y' == input('Correct the files in current directory?'):
        names = glob.glob('*.fits')



    
else:
    names = glob.glob(f'{directory}/*.fits')


    for i, name in enumerate(names):
        data =np.float32(fits.getdata(name))

        hdu = (fits.PrimaryHDU(data))

        os.remove(name)
        hdu.writeto(f'{directory}/{i}.fits', overwrite=True)

