# Script to convert the XML annotations to the desired YOLO format 
import os
import xml.etree.ElementTree as ET
import argparse
 
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--pascal", required=True,
help="path to xml annotations directory")
ap.add_argument("-y", "--yolo", required=True,
help="path to txt format directory")
args = vars(ap.parse_args())

 
for filepath in os.listdir(args["pascal"]):
 
    root = ET.parse(os.path.join(args["pascal"],filepath)).getroot()
 
    xmin, ymin, xmax, ymax = 0,0,0,0
    size = root.find('size')
    width = float(size[0].text)
    height = float(size[1].text)
    filename = root.find('filename').text
    for child in root.findall ( 'object'): # find all the boxes in the picture
        sub = child.find ('bndbox') # find the dimension values ​​and reading frame
        label = child.find('name').text
        if label == 'helmet':
            label = 0
        elif label == 'head':
            label = 1
        xmin = float(sub[0].text)
        ymin = float(sub[1].text)
        xmax = float(sub[2].text)
        ymax = float(sub[3].text)
                 
        x_center = (xmin + xmax) / (2 * width)
        y_center = (ymin + ymax) / (2 * height)
        w = (xmax - xmin) / width
        h = (ymax - ymin) / height
 
        with open(os.path.join(args["yolo"], filepath.split('.')[0]+'.txt'), 'a+') as f:
            f.write(' '.join([str(label), str(x_center), str(y_center), str(w), str(h) + '\n']))
 
print('Completed.')