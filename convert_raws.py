import numpy as np
import glob, os
from sizes import *
import tifffile as tiff
import math

def getClosestFactors(val):
    testNum = int(math.sqrt(val))
    while (val % testNum != 0):
        testNum -= 1

    a = testNum
    b = val / testNum

    if a < b:
        a, b = b, a
    return (int(a), int(b))

os.chdir('./raws')
for f in glob.glob('*.RAW'):
    size = os.path.getsize (f)
    scan_info = {}
    height = 0
    width = 0

    if str(size) in sizes.keys():
        scan_info = sizes[str(size)]
        height = scan_info['psheight']
        width = scan_info['pswidth']
        print(f, ' - ', size, ' bytes - ', scan_info['format'])
    else:
        height, width = getClosestFactors(size / 6)
    
    
    basename = os.path.basename(f)
    rawpath = os.path.abspath(f)
    raw = np.fromfile(rawpath, np.uint16)
    filename_no_ext = os.path.splitext(rawpath)[0]
    # raw8 = np.fromfile(rawpath, np.uint8)

    print('RAW :\n\t', len(raw), raw)
    # print('RAW8 :\n\t', len(raw8), raw8)


    r = raw[0::3].copy()
    g = raw[1::3].copy()
    b = raw[2::3].copy()    

    rgb = np.dstack((b, g, r)).reshape((height, width, 3))
    rgb *= (65536 // 4096) # Convert the 12-bits value to 16-bits, Noritsu RAWs are 12-bits but packed into 16-bits chunks

    crop_percent = 5
    crop_height = int (crop_percent * height / 100)
    crop_width = int (crop_percent * width / 100)
    rgb = rgb[crop_height:-crop_height, crop_width:-crop_width,:]
    rgb = np.rot90(rgb, 3)
    tiff.imsave(filename_no_ext + '.tiff', rgb, dtype=np.uint16)

    # print(rgbflat)