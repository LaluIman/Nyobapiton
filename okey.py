import numpy as np
import pandas as pd
import tensorflow as tf

# Inisialisasi model
model = tf.keras.models.Sequential([
  tf.keras.layers.Embedding(10000, 128),
  tf.keras.layers.LSTM(128),
  tf.keras.layers.Dense(10000)
])

# Inisialisasi data
data = pd.read_csv("data.csv")

# Latih model
model.compile(optimizer="adam", loss="categorical_crossentropy")
model.fit(data["text"].to_numpy(), data["label"].to_numpy(), epochs=10)

def chat(text):
  # Prediksi label dari teks
  prediction = model.predict(np.array([text]))

  # Kembalikan label yang paling mungkin
  return data["label"].iloc[np.argmax(prediction)]

# Mulai percakapan
while True:
  # Terima input dari pengguna
  text = input("Masukkan teks: ")

  # Proses input
  label = chat(text)

  # Tampilkan respons
  print("Label:", label)
