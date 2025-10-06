import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# 1. Generate simple sequential data
# Example: input [0,1,2] -> output [3]
sequence = np.array([i for i in range(50)], dtype=np.float32)
window_size = 3

X, Y = [], []
for i in range(len(sequence) - window_size):
    X.append(sequence[i:i+window_size])
    Y.append(sequence[i+window_size])

X = np.array(X)
Y = np.array(Y)

# Reshape to LSTM expected input: [samples, timesteps, features]
X = X.reshape((X.shape[0], X.shape[1], 1))

# 2. Build LSTM model
model = Sequential([
    LSTM(50, activation='tanh', input_shape=(window_size, 1)),
    Dense(1)
])

# 3. Compile model
model.compile(optimizer='adam', loss='mse')

# 4. Train model
model.fit(X, Y, epochs=300, verbose=0)

# 5. Test prediction
test_input = np.array([47, 48, 49], dtype=np.float32).reshape((1, window_size, 1))
pred = model.predict(test_input, verbose=0)
print(f"Predicted next value after [47,48,49]: {pred[0][0]:.2f}")

# 6. Save the model
model.save("lstm_model.keras")
print("Model saved to lstm_model.h5")
