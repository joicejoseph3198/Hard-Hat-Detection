# HardHatDetection
 Using Yolov5 to build a object detection model to detect hard hats and additionally change the the color of the bounding box to match the color of the hard hats detected by the model.


### Dataset
The dataset contains 4,750 images of hard hats with their respective labels, and 250 test images without labels.
I also use a video to run inference on, to see the real time performance of the model.

### Model 
The object detection model used is Yolov5. I've made the use of github repository maintained by 'Ultralytics' and tweaked their code to train the model and get the desired result.

So what I did was:
- clone the git repo
- change the original XML labels to YOLO format
- get the data in proper directory structure 
- Creat a YAML file to provide the training/val folder and provide the class name and other configurations
- train the model
- run the inference on test images
- run the inference on test video

The code I added to get the hard hat color
![Project Image1](https://github.com/joicejoseph3198/Images/blob/main/code.JPG)

![Project Image2](https://github.com/joicejoseph3198/Images/blob/main/Screenshot-20210728200926-1900x1000.png)
I trained my model for about 40 epochs and i got mAP score of nearly 0.93 which seemed pretty good. I could've have got better results had I trained it for more epochs. But considering my computational power, this seemed good enough.

![Project Image3](https://github.com/joicejoseph3198/Images/blob/main/results.png)

Result of the training turned out to look like this:
![Project Image4](https://github.com/joicejoseph3198/Images/blob/main/hard_hat_workers1294.png)
![Project Image10](https://github.com/joicejoseph3198/Images/blob/main/hard_hat_workers1543.png)
![Project Image5](https://github.com/joicejoseph3198/Images/blob/main/hard_hat_workers1684.png)
![Project Image6](https://github.com/joicejoseph3198/Images/blob/main/hard_hat_workers210.png)
![Project Image7](https://github.com/joicejoseph3198/Images/blob/main/hard_hat_workers2899.png)
![Project Image8](https://github.com/joicejoseph3198/Images/blob/main/hard_hat_workers509.png)
![Project Image9](https://github.com/joicejoseph3198/Images/blob/main/hard_hat_workers91.png)

Screenshots from the inference video:
![Project Image11](https://raw.githubusercontent.com/joicejoseph3198/Images/blob/main/Capture1.JPG)
![Project Image12](https://raw.githubusercontent.com/joicejoseph3198/Images/blob/main/Capture2.JPG)
![Project Image13](https://raw.githubusercontent.com/joicejoseph3198/Images/blob/main/Capture3.JPG)
![Project Image14](https://raw.githubusercontent.com/joicejoseph3198/Images/blob/main/Capture4.JPG)
![Project Image15](https://raw.githubusercontent.com/joicejoseph3198/Images/blob/main/Capture5.JPG)
![Project Image16](https://raw.githubusercontent.com/joicejoseph3198/Images/blob/main/Capture6.JPG)
![Project Image17](https://raw.githubusercontent.com/joicejoseph3198/Images/blob/main/Capture7.JPG)
