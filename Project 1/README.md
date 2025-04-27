# 🌾 Rice Leaf Disease Prediction - Project 1
This is Project 1 of the Rice Leaf Disease Prediction series.<br>
In this project, we built a deep learning model from scratch to classify rice leaf diseases and created an interactive Streamlit web application for easy usage.

## 🚀 Technologies Used:
 - TensorFlow – For building and training the model
 - Keras – For model creation and layers
 - scikit-learn – For evaluation and metrics
 - matplotlib – For plotting and visualization
 - pickle – For saving and loading trained models
 - Streamlit – For building the interactive web app

## 📈 How the Project Works:
  - Model Training:<br>
    Images were preprocessed and fed into a Convolutional Neural Network (CNN) using TensorFlow and Keras.<br>
    After training, the model was saved using joblib.
  - Web Application:<br>
    A simple Streamlit app allows users to upload an image of a rice leaf.<br>
    The model predicts whether the leaf is healthy or affected by a specific disease.
  - Testing & Evaluation:<br>
    scikit-learn was used for performance metrics.<br>
    matplotlib visualized training accuracy, loss graphs, and confusion matrices.

## 📥 How to Run Locally:
  - Run "streamlit run RiceLeafDiseasePrediction_WebBased.py" in your Python Terminal
