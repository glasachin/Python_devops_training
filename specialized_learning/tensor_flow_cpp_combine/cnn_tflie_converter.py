import tensorflow as tf

# 1. Load the Keras model
model = tf.keras.models.load_model("cnn-model.keras")   # or cnn.h5

# 2. Convert to TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# (Optional) Enable optimizations (for size/speed)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# 3. Convert the model
tflite_model = converter.convert()

# 4. Save the TFLite model to file
with open("cnn-model.tflite", "wb") as f:
    f.write(tflite_model)

print("✅ Conversion successful! Saved as cnn.tflite")
