# 🚀 Rice Leaf Disease Prediction – Project 3

## 📋 Project Description
This project is the third part of the Rice Leaf Disease Prediction series.<br>
In this project, the complete Streamlit web application has been dockerized using Docker Desktop.<br>

The containerized application allows easy deployment across different environments without worrying about dependencies.

## 🛠 Technologies Used
  - Docker Desktop
  - Python 3

## Docker File Contents
```
# Use official Python base image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy all files from your local folder to the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Command to run your Streamlit app
CMD ["streamlit", "run", "RiceLeafDisease_PreTrained_WebBased.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## 🐳 Common Docker Commands Used
 1. Build Docker Image:
```docker build -t riceleaf_dockerimage .```<br>
-t give tag(name) to the image.

 2. Run Docker Container:
```docker run -p 8501:8501 riceleaf_dockerimage```<br>
-p 8501:8501 maps the local port to the container port.

 3. Save Docker Image (Optional Backup):
```docker save -o riceleaf_dockerimage.tar riceleaf_dockerimage```<br>
This saves the image as a .tar file, useful for sharing without rebuilding.

## 📢 Important Notes
  - Docker Desktop must be installed and running.
  - You must build the image before running the container.
  - The requirements.txt should list all Python libraries needed by the app.
  - Once the container is up and running, you can open your browser and visit:
    ```http://localhost:8501 ``` 
## 📦 Steps to Create a Docker Image for Your Project
  1. Make a Folder/Create a new folder<br>
     Put all these inside the folder:
     - Your project files (Python files, saved model files, requirements.txt, Dockerfile, etc.)
     - ❌ Don't put the README.md (not needed inside Docker image).
  2. Open Command Line Interface (CLI)
  3. Go to Your Project Folder
     - Use the cd command to go inside your project folder.
  4. Build the Docker Image
  5. Run the Docker Image
  6. Save Your Docker Image (Optional Backup)
