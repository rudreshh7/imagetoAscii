import sys, random, argparse
import numpy as np
import math

from PIL import Image

#gray scale level values from:

#70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# 10 Levels of Gray
gscale2 = "@%#*+=-:. "


def getAverageL(image):
    im = np.array(image)

    w, h = im.shape

    return np.average(im.reshape(w*h))

def convertImagetoASCII(filename, cols, scale, moreLevels):
    global gscale1, gscale2
    image = Image.open(filename).convert('L')
    W , H = image.size[0],image.size[1]
    w = W/cols
    h = w/scale
    rows = int(H/h)
    if cols > W or rows > H:
        print("Image Size is too small for specified cols")
        exit(0)
    aimg = []
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)
        if j == rows-1:
            y2 = H
        aimg.append("")
        for i in range(cols):
            x1 = int(i*w)
            x2 = int((i+1)*w)
            if i == cols-1:
                x2 = W
            img = image.crop((x1, y1, x2, y2))
            avg = int(getAverageL(img))
            if moreLevels:
                gsval = gscale1[int((avg*69)/255)]
            else:
                gsval = gscale2[int((avg*9)/255)]
            aimg[j] += gsval
    return aimg
# main function

def main():
    #create parser
    descStr = "This program converts an Image into ASCII art."
    parser = argparse.ArgumentParser(description=descStr)

    # add expected arguements
    parser.add_argument('--file', dest='imgFile',required = True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='outFile',required=False)
    parser.add_argument('--cols',dest='cols',required=False)
    parser.add_argument('--moreLevels',dest='moreLevels',action='store_true')

    # parse args
    args = parser.parse_args()

    imgFile = args.imgFile

    # set output file
    outfile = 'out.txt'

    if args.outFile:
        outFile = args.outFile

    scale = 0.43
    if args.scale:
        scale = float(args.scale)

    #set cols
    cols = 80
    if args.cols:
        cols = int(args.cols)

    print('Generating ASCII art...')
    aimg = convertImagetoASCII(imgFile, cols, scale, args.moreLevels)
    # open file
    f = open(outFile, 'w')

    # # write to file
    for row in aimg:
        f.write(row + '\n')

    # cleanup
    f.close()
    print("ASCII art written to %s" % outFile)

# call main
if __name__ == '__main__':
    main()

# $python "main.py" --file data/11.jpg --cols 120















