import numpy as np
import cv2
from tensorflow.keras.models import load_model

import streamlit as st

# load model
model = load_model('models/dog_breed_67.h5')

labels = ['afghan_hound', 'maltese_dog', 'scottish_deerhound']

# title of the app
st.title("Dog Breed Classifier")
st.markdown("Upload an image of a dog and we identify the breed for you")

#
dog_image = st.file_uploader("Choose image to upload", type="jpg")
submit = st.button('Predict')

# on predict button click
if submit:
    if dog_image is not None:

        # have the image as a numpy array to use on opencv
        img_file_array = np.asarray(bytearray(dog_image.read()), dtype=np.uint8)
        open_cv_img = cv2.imdecode(img_file_array,1)

        # displaying the image
        st.image(open_cv_img,channels='BGR')
        #resize the image
        open_cv_img = cv2.resize(open_cv_img,(224,224))
        #reshaping the image
        open_cv_img.shape = (1,224,224,3)
        y_pred = model.predict(open_cv_img)

        st.title(f"The dog breed is {labels[np.argmax(y_pred)]}")

