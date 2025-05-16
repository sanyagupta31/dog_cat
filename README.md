
---

````markdown
# 🐶🐱 Dog vs Cat Classifier
---

A simple web app built with **Streamlit** and **TensorFlow** to classify images as either a **dog** or a **cat**.
---

## 📌 Features

- Upload an image (JPG, JPEG, PNG)
- The model predicts whether it's a dog or a cat
- Clean, user-friendly UI with Streamlit

## 🧠 Model

- Trained using TensorFlow/Keras
- Input image size: 64x64x3
- Binary classification: Dog (1) or Cat (0)

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sanyagupta31/dog-cat.git
cd dog-cat
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

## 📝 Requirements

* streamlit
* tensorflow
* numpy
* pillow

All listed in `requirements.txt`.

## 📸 Example

Upload an image like:

![Sample](example_image.jpg)

You'll get a prediction like:

```
🎉 It's a Dog! 🐶
```

or

```
🎉 It's a Cat! 🐱
```

## 🙌 Acknowledgements

Model trained on a subset of the Dogs vs Cats dataset from Kaggle.
Built using Streamlit, TensorFlow, and Python.



