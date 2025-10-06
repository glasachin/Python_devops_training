import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# 1. Load the trained model
model = load_model("lstm_model.keras")

# 2. Prepare input data
window_size = 3
test_input = np.array([47, 48, 49], dtype=np.float32).reshape((1, window_size, 1))

# 3. Run inference
pred = model.predict(test_input, verbose=0)

# 4. Print prediction
print(f"Predicted next value after [47, 48, 49]: {pred[0][0]:.2f}")
