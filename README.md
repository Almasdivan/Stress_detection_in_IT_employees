## Dataset

The dataset used for this project contains facial expression images for training and evaluating the CNN-based emotion detection model.

### Emotion Classes

The dataset contains images categorized into the following emotion classes:

- Angry
- Disgust
- Fear
- Happy
- Sad
- Surprise
- Neutral

### Dataset Structure

The dataset is divided into:

- `train/` – Images used for training the CNN model.
- `test/` – Images used for evaluating the trained model.
- `validation/` – Images used for validation during model development.

> The dataset is not included in this repository due to dataset size and/or licensing considerations.



# Emotion_detection_with_CNN

![emotion_detection](https://github.com/datamagic2020/Emotion_detection_with_CNN/blob/main/emoition_detection.png)

### Packages need to be installed
- pip install numpy
- pip install opencv-python
- pip install keras
- pip3 install --upgrade tensorflow
- pip install pillow

### download FER2013 dataset
- from below link and put in data folder under your project directory
- https://www.kaggle.com/msambare/fer2013

### Train Emotion detector
- with all face expression images in the FER2013 Dataset
- command --> python TranEmotionDetector.py

It will take several hours depends on your processor. (On i7 processor with 16 GB RAM it took me around 4 hours)
after Training , you will find the trained model structure and weights are stored in your project directory.
emotion_model.json
emotion_model.h5

copy these two files create model folder in your project directory and paste it.

### run your emotion detection test file
python TestEmotionDetector.py


