# To create a validation set
import os
import shutil
import numpy as np
import random

image_dir ="H:/Python Space/Hard_Hat _Detection/images"
label_dir= "H:/Python Space/Hard_Hat _Detection/labels"
destination1 = "/val"
destination2 = "/train"


img_list= []
label_list= []


for file in os.listdir(image_dir):
    if os.path.isfile(label_dir + "/" + file[:-4]+".txt"): # that is to see if the annotation of the image exists
        img_list.append(file)
        label_list.append(file[:-4]+".txt")
    else:
        continue # skip over the image with no annotation


# moving images and labels into val directory
for filename in random.sample(img_list, int(len(img_list) *.2)):
        shutil.move(image_dir + "/" + filename, image_dir + "/" + destination1)
        shutil.move(label_dir + "/" + filename[:-4]+".txt", label_dir + "/" + destination1)
        img_list.remove(filename)
print("Validation dataset created.")

# move the remaining images and annotations to the train directory
for filename in img_list:
    shutil.move(image_dir + "/" + filename, image_dir + "/" + destination2)
    shutil.move(label_dir + "/" + filename[:-4]+".txt", label_dir + "/" + destination2)
print("Training dataset created.")
