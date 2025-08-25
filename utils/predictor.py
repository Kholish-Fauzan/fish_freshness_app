import numpy as np
import tensorflow as tf
from PIL import Image
import os
from tensorflow.keras.applications.vgg16 import preprocess_input as vgg16_preprocess

def predict_image(image: Image.Image):
    """
    Melakukan prediksi menggunakan model TensorFlow Lite.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, "..", "models", "vgg16_finetune_quantized.tflite")
    labels_path = os.path.join(current_dir, "..", "labels", "labels.txt")

    # Load model TFLite
    try:
        interpreter = tf.lite.Interpreter(model_path=model_path)
        interpreter.allocate_tensors()
    except Exception as e:
        print(f"Error saat memuat model: {e}")
        return "Terjadi kesalahan saat memuat model.", 0.0, {}

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    input_shape = input_details[0]['shape']

    # Pra-pemrosesan gambar
    resized_image = image.resize((input_shape[1], input_shape[2]))
    image_array = np.array(resized_image, dtype=np.float32)
    image_array = vgg16_preprocess(image_array)

    # Tambahkan dimensi batch
    image_array = np.expand_dims(image_array, axis=0)

    # Jalankan inferensi
    interpreter.set_tensor(input_details[0]['index'], image_array)
    interpreter.invoke()

    # Dapatkan hasil
    output_data = interpreter.get_tensor(output_details[0]['index'])[0]
    print(f"Output model mentah: {output_data}")

    # Load label
    try:
        with open(labels_path, "r") as f:
            labels = [line.strip() for line in f.readlines()]
    except Exception as e:
        print(f"Error saat memuat label: {e}")
        return "Terjadi kesalahan saat memuat label.", 0.0, {}
    
    # Dapatkan indeks dan nilai keyakinan tertinggi
    predicted_index = np.argmax(output_data)
    confidence = np.max(output_data)

    # Dapatkan skor probabilitas untuk semua kelas
    confidence_scores = {labels[i]: float(output_data[i]) for i in range(len(labels))}

    # Ambil label berdasarkan indeks yang diprediksi
    predicted_label = labels[predicted_index]
    confidence_percentage = f"{confidence * 100:.2f}"

    return predicted_label, confidence_percentage, confidence_scores