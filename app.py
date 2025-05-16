import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Title
st.title("Dog vs Cat Classifier 🐶🐱")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Load trained model (make sure 'model.h5' exists in the same directory)
model = tf.keras.models.load_model("dog_cat_classifier.h5")

if uploaded_file is not None:
    # Display image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess image
    img = image.resize((64, 64)).convert('RGB')  # Ensure 3 channels (RGB)
    img_array = np.array(img) / 255.0  # Normalize pixel values
    img_array = img_array.reshape(1, 64, 64, 3)  # Add batch dimension

    # Predict button
    if st.button("Predict"):
        prediction = model.predict(img_array)

        # Assuming binary classification with sigmoid activation
        class_label = "Dog 🐶" if prediction[0][0] > 0.5 else "Cat 🐱"
        confidence = float(prediction[0][0]) if prediction[0][0] > 0.5 else 1 - float(prediction[0][0])

        st.write(f"**Prediction:** {class_label}")
        st.write(f"**Confidence:** {confidence:.2%}")
