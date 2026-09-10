import cv2
import os

# Define the paths to the train and test datasets
train_dataset_path = "/data/train"
test_dataset_path = "/data/train"

# Load the train dataset
train_dataset = []
train_labels = []
for folder in os.listdir(train_dataset_path):
    folder_path = os.path.join(train_dataset_path, folder)
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            image = cv2.imread(file_path)
            train_dataset.append(image)
            train_labels.append(folder)

# Load the test dataset
test_dataset = []
test_labels = []
for folder in os.listdir(test_dataset_path):
    folder_path = os.path.join(test_dataset_path, folder)
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            image = cv2.imread(file_path)
            test_dataset.append(image)
            test_labels.append(folder)

# Remove duplicates in the train dataset
hashes = []
indices = []
for i, image in enumerate(train_dataset):
    hash = cv2.img_hash.pHash(image)
    if hash in hashes:
        indices.append(i)
    else:
        hashes.append(hash)
train_dataset = [image for i, image in enumerate(train_dataset) if i not in indices]
train_labels = [label for i, label in enumerate(train_labels) if i not in indices]

# Remove irrelevant images in the train dataset
haar_cascade_path = "/path/to/haarcascade_frontalface_default.xml"
face_detector = cv2.CascadeClassifier(haar_cascade_path)
indices = []
for i, image in enumerate(train_dataset):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray)
    if len(faces) == 0:
        indices.append(i)
train_dataset = [image for i, image in enumerate(train_dataset) if i not in indices]
train_labels = [label for i, label in enumerate(train_labels) if i not in indices]

# Remove irrelevant images in the test dataset
indices = []
for i, image in enumerate(test_dataset):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray)
    if len(faces) == 0:
        indices.append(i)
test_dataset = [image for i, image in enumerate(test_dataset) if i not in indices]
test_labels = [label for i, label in enumerate(test_labels) if i not in indices]

# Save the cleaned datasets
cleaned_train_dataset_path = "/data/cleaned/train"
cleaned_test_dataset_path = "/data/cleaned/test"
if not os.path.exists(cleaned_train_dataset_path):
    os.makedirs(cleaned_train_dataset_path)
if not os.path.exists(cleaned_test_dataset_path):
    os.makedirs(cleaned_test_dataset_path)
for label in set(train_labels):
    label_path = os.path.join(cleaned_train_dataset_path, label)
    if not os.path.exists(label_path):
        os.mkdir(label_path)
for image, label in zip(train_dataset, train_labels):
    label_path = os.path.join(cleaned_train_dataset_path, label)
    image_path = os.path.join(label_path, os.path.basename(file))
    cv2.imwrite(image_path, image)
for label in set(test_labels):
    label_path = os.path.join(cleaned_test_dataset_path, label)
    if not os.path.exists(label_path):
        os.mkdir(label_path)
for image, label in zip(test_dataset, test_labels):
    label_path = os.path.join(cleaned_train_dataset_path, label)
    image_path = os.path.join(label_path, os.path.basename(file))
    cv2.imwrite(image_path, image)
