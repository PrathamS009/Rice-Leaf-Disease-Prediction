import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

tf.keras.backend.clear_session()
Model = load_model("RiceLeafDiseaseModel_New.keras")
dataset = tf.keras.preprocessing.image_dataset_from_directory("RiceLeafDisease - Dataset/train")
class_labels = dataset.class_names
print(class_labels)

def preprocess_img(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224,224))
    img = np.array(img)/255.0
    img = np.expand_dims(img, axis=0)
    return img

image_path = "RiceLeafDisease - Dataset/Validation/Hispa/RiceHispa(39).jpg"

input_img = preprocess_img(image_path)

prediction = Model.predict(input_img)

predicted_class = class_labels[np.argmax(prediction, axis=1)[0]]


print(f"Predicted Class is: {predicted_class}\nPrediction is: {prediction}")