import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

model = load_model("lstm_model.keras")
# Convert to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS,     # TFLite ops
    tf.lite.OpsSet.SELECT_TF_OPS        # TensorFlow ops
]
converter._experimental_lower_tensor_list_ops = False
converter.experimental_enable_resource_variables = True

tflite_model = converter.convert()
with open("lstm_model.tflite", "wb") as f:
    f.write(tflite_model)

print("Saved TensorFlow Lite model to lstm_model.tflite")
