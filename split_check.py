import os

image_dir ="H:/Python Space/Hard_Hat _Detection/images"
label_dir= "H:/Python Space/Hard_Hat _Detection/labels"

print("No. of Training images", len(os.listdir(image_dir + "/train")))
print("No. of Training labels", len(os.listdir(label_dir + "/train")))

print("No. of valid images", len(os.listdir(image_dir + "/val")))
print("No. of valid labels", len(os.listdir(label_dir + "/val")))
