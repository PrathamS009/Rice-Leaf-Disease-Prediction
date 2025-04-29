import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:io';
import 'package:tflite/tflite.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  File? _image;
  List<dynamic>? _predictionResult;
  final picker = ImagePicker();

  @override
  void initState() {
    super.initState();
    loadModel();
  }

  // Load the TFLite model
  Future<void> loadModel() async {
    String? res = await Tflite.loadModel(
      model: "assets/rice_leaf_model.tflite",
      labels: "assets/labels.txt",
    );
    print("Model load result: $res");
  }

  // Pick image
  Future<void> _getImage(ImageSource source) async {
    final pickedFile = await picker.pickImage(source: source);

    if (pickedFile != null) {
      setState(() {
        _image = File(pickedFile.path);
        _predictionResult = null;
      });
    }
  }

  // Run prediction
  Future<void> _predictImage(File? image) async {
    if (image == null) return;

    var output = await Tflite.runModelOnImage(
      path: image.path,
      imageMean: 0.0,
      imageStd: 255.0,
      numResults: 3,
      threshold: 0.5,
      asynch: true,
    );

    setState(() {
      _predictionResult = output;
    });
  }

  @override
  void dispose() {
    Tflite.close();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Rice Leaf Disease Detection',
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Rice Leaf Disease Detection'),
          centerTitle: true,
        ),
        body: SingleChildScrollView(
          padding: const EdgeInsets.all(16),
          child: Column(
            children: [
              _image == null
                  ? const Text('📷 No image selected.')
                  : Image.file(_image!),
              const SizedBox(height: 16),

              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  ElevatedButton.icon(
                    onPressed: () => _getImage(ImageSource.camera),
                    icon: const Icon(Icons.camera_alt),
                    label: const Text("Camera"),
                  ),
                  ElevatedButton.icon(
                    onPressed: () => _getImage(ImageSource.gallery),
                    icon: const Icon(Icons.photo_library),
                    label: const Text("Gallery"),
                  ),
                ],
              ),

              const SizedBox(height: 16),

              ElevatedButton(
                onPressed: () => _predictImage(_image),
                child: const Text("🔍 Predict"),
              ),

              const SizedBox(height: 24),

              if (_predictionResult != null && _predictionResult!.isNotEmpty)
                Column(
                  children: [
                    Text(
                      "🌿 Disease Detected: ${_predictionResult![0]['label']}",
                      style: const TextStyle(
                        fontSize: 22,
                        fontWeight: FontWeight.bold,
                        color: Colors.green,
                      ),
                    ),
                    const SizedBox(height: 8),
                    Text(
                      "Confidence: ${(_predictionResult![0]['confidence'] * 100).toStringAsFixed(2)}%",
                      style: const TextStyle(fontSize: 18),
                    ),
                    const SizedBox(height: 16),
                    ElevatedButton(
                      onPressed: () {
                        setState(() {
                          _image = null;
                          _predictionResult = null;
                        });
                      },
                      child: const Text("Predict Again"),
                    )
                  ],
                )
            ],
          ),
        ),
      ),
    );
  }
}
