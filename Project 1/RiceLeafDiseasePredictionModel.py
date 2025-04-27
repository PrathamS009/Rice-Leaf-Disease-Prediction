import pickle
import keras
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.layers import GlobalAveragePooling2D
from tensorflow.keras.regularizers import l2
from tensorflow.keras.optimizers import SGD

training_folder = "RiceLeafDisease - Dataset/Train"
validation_folder = "RiceLeafDisease - Dataset/Validation"

training_data = tf.keras.utils.image_dataset_from_directory(
    training_folder,
    image_size  = (224,224),
    batch_size = 32,
    shuffle = True,
    label_mode = "categorical"
)

validation_data = tf.keras.utils.image_dataset_from_directory(
    validation_folder,
    image_size = (224,224),
    batch_size = 32,
    label_mode = "categorical"
)

# IMAGE_SIZE = (256,256)

class_names = training_data.class_names
print("Classes of training data: ", class_names)

# To Display some images
    # plt.figure(figsize=(10,10))
    # for images, labels in training_data.take(1):
    #     for i in range(9):
    #         plt.subplot(3,3,i+1)
    #         plt.imshow(images[i].numpy().astype("uint8"))
    #         plt.title(class_names[labels[i].numpy()])
    #         plt.axis("off")
    # plt.show()

# training_dataset = training_data.map(lambda x, y:(tf.image.resize(x, IMAGE_SIZE), y))
# validation_dataset = validation_data.map(lambda x, y:(tf.image.resize(x, IMAGE_SIZE), y))

normalization_layer = tf.keras.layers.Rescaling(1.0/255)

@tf.function
def normalize_image(x, y):
    x = normalization_layer(x)
    return x, y

training_dataset = training_data.map(normalize_image)
validation_dataset = validation_data.map(normalize_image)


AUTOTUNE = tf.data.AUTOTUNE
training_dataset = training_dataset.prefetch(buffer_size=AUTOTUNE)
validation_dataset = validation_dataset.prefetch(buffer_size=AUTOTUNE)

# data_augmentation = keras.Sequential([
#     layers.RandomFlip("horizontal"),
#     layers.RandomRotation(0.1),
#     layers.RandomZoom(0.1),
#     layers.RandomContrast(0.1),
#     layers.RandomBrightness(0.1),
#     # layers.RandomTranslation(height_factor=0.1, width_factor=0.1)
# ])

# training_dataset = training_dataset.map(lambda x, y: (print(x.shape) or tf.squeeze(data_augmentation(tf.ensure_shape(x, (None, 256, 256, 3)), training=True)), y))

# def augment_data(x, y):
#     x = data_augmentation(x, training=True)
#     return x, y
#
# training_dataset = training_dataset.map(augment_data)


RiceLeafDiseasePrediction_Model = keras.Sequential([
    layers.Conv2D(32, (3,3), activation="relu", input_shape=(224, 224, 3)),
    layers.MaxPooling2D(pool_size=(2,2)),

    layers.Conv2D(64, (3,3), activation="relu"),
    layers.MaxPooling2D(pool_size=(2,2)),

    layers.Conv2D(128, (3,3), activation="relu"),
    layers.MaxPooling2D(pool_size=(2,2)),

    # layers.Flatten(),

    GlobalAveragePooling2D(),

    layers.Dense(128, activation="relu", kernel_regularizer=l2(0.01)),

    layers.Dropout(0.3),

    layers.Dense(5, activation="softmax")
])

# RiceLeafDiseasePrediction_Model.summary()

for image, label in training_dataset.take(1):
    print("Image shape:", image.shape)
    print("Label shape:", label.shape)
    print("Image dtype:", image.dtype)
    print("Label dtype:", label.dtype)

optimizer=SGD(learning_rate=0.01, momentum=0.9)
RiceLeafDiseasePrediction_Model.compile(
    optimizer=optimizer,
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

Model_Training = RiceLeafDiseasePrediction_Model.fit(
    training_dataset,
    validation_data = validation_dataset,
    epochs = 5
)

with open("Model_Training_History.pkl","wb") as f:
    pickle.dump(Model_Training.history, f)

RiceLeafDiseasePrediction_Model.save("RiceLeafDiseaseModel_Fast.keras")