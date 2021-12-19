# Dog Breed Classifier
A simple A web application that classifies dog images into one of 3 dog breeds i.e afghan_hound, maltese_dog, & scottish_deerhound. 
The model was trained using tensorflow without transfer learning and the web application built using streamlit.

# Requirements
- [Tensorflow](https://streamlit.io/) (Library to build and train neural networks in Tensorflow)
- [Streamlit](https://streamlit.io/) (Library to build web apps in python) 
- [Numpy](https://numpy.org/) (Library for numerical computations)
- [pandas](https://pandas.pydata.org/) (Library that helps us load the data into tabular formats) 
- [Opencv](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) (Image processing library in python)

# Table Of Contents
-  [In a Nutshell](#in-a-nutshell)
-  [In Details](#in-details)
-  [Future Work](#future-work)
-  [Contributing](#contributing)
-  [Acknowledgments](#acknowledgments)

# In a Nutshell   
In a nutshell here's how to run this application:
- Create an environment with either anaconda or pip
- Start the environment and install the requirements by running **pip install -r 'requirements.txt'**
- Switch to the project directory and run **streamlit run app.py** .This will start the streamlit app in your browser. 
You can then upload images of dogs and get the class prediction using the trained model.

To Train your own model
-Open the **main.ipynb** and update the model parameters as required and it will save your model in the models folder



# In Details
```
├── app.py            - Script to generate our web application
├── main.ipynb        - Notebook that is used to build,train and evaluate the model
├── data
│   ├── test    - this folder contains the test image data
│   └── train   - this folder contains the train image data
├── models            - this folder contains the models with various accuracies
│   └── dog_breed_67.h5 - model with 67% accuracy
├── README.md
└── requirements.txt  - Has the requirements needed to run the project

```


# Future Work
Apply transfer learning to the model

# Contributing
Any kind of enhancement or contribution is welcomed.

# Acknowledgments
Datasets for the project is here https://www.kaggle.com/c/dog-breed-identification
