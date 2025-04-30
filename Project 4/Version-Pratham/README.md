

# 🌾 Rice Leaf Disease Prediction App (Flutter + TFLite)

A mobile application built using **Flutter** and **TensorFlow Lite** to detect diseases in rice leaves using deep learning. The app allows users to upload an image of a rice leaf and instantly get predictions about its health condition — even offline!

---

## 📱 Features

- Detects rice leaf diseases from images.
- Works completely offline using a TFLite model.
- Clean and user-friendly interface.
- Built using Flutter, TFLite, and TensorFlow.
- Supports Android (APK build ready).

---

## 🧠 Model Overview

The model is a custom **Convolutional Neural Network (CNN)** trained on a rice leaf disease dataset with multiple classes:

- Healthy
- Bacterial Leaf Blight
- Brown Spot
- Leaf Smut

The trained Keras model was converted to **TensorFlow Lite (TFLite)** for efficient on-device inference.

---

## 🛠️ Tech Stack

- **Flutter** – UI and app logic.
- **TFLite** – On-device machine learning inference.
- **TensorFlow / Keras** – For training the model.
- **Python** – For data preprocessing and model conversion.

---

## 📂 Folder Structure

```
rice_leaf_disease_prediction/
├── assets/
│   ├── rice_model.tflite
│   └── labels.txt
├── lib/
│   └── main.dart
├── android/
│   └── app/
│        └── (Updated Gradle files)
├── pubspec.yaml
```


## 📦 Dependencies

In `pubspec.yaml`:

```yaml
dependencies:
  flutter:
    sdk: flutter
  tflite: ^1.1.2
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/rice_leaf_disease_prediction.git
cd rice_leaf_disease_prediction
```

### 2. Install Flutter Packages

```bash
flutter pub get
```

### 3. Add Your Model and Labels

Make sure `assets/rice_model.tflite` and `assets/labels.txt` are present and listed in `pubspec.yaml`.

```yaml
assets:
  - assets/rice_model.tflite
  - assets/labels.txt
```

### 4. Fix Android Build Environment

- Use **JDK 17**.
- In `android/gradle.properties`:
  ```properties
  org.gradle.java.home=D:\\Java-JDK\\JDK-17
  ```

- In `android/app/build.gradle`, set:
  ```gradle
  compileSdkVersion 34
  ```

- In the `tflite` plugin's `build.gradle` (under `.pub-cache`), replace:
  ```gradle
  compile 'org.tensorflow:tensorflow-lite:+'
  ```
  with:
  ```gradle
  implementation 'org.tensorflow:tensorflow-lite:+'
  ```

---

## 🚀 Run the App

```bash
flutter run
```

---

## 📦 Build APK

```bash
flutter build apk --release
```

Find the APK here:

```
build/app/outputs/flutter-apk/app-release.apk
```

---

## 📌 Notes

- You may see deprecation warnings from the `tflite` plugin — safe to ignore.
- Works best on real Android devices or emulator with camera/gallery access.

---

## ✨ Future Improvements

- Add camera support.
- Improve model accuracy with a larger dataset.
- Add support for real-time detection.

---

## 🧑‍💻 Author

Made with 💻 and 🧠 by:
  - Pratham Singh

