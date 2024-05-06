# Car-price-prediction

In this project, we have developed a machine learning model to predict the selling price of cars based on various features such as brand name, manufacturing year, kilometers driven, fuel type, seller type, transmission type, owner type, mileage, engine capacity, maximum power, and number of seats.

## Project Overview

We have built a linear regression model using the scikit-learn library in Python. The model is trained on a dataset containing car details and their corresponding selling prices. After preprocessing the data and training the model, we have saved the trained model as a pickle file (`car_model.pkl`) for future use.

## Important Note

To deploy the car price prediction model in the `app.py` file, please ensure to follow these steps:

1. **Notebook Execution**: Execute all the steps provided in the Jupyter Notebook (`car_price.ipynb`) or any other notebook where the model was developed. This includes data loading, preprocessing, feature engineering, model training, and evaluation.

2. **Export Trained Model**: After training the model successfully in the notebook, save the trained model as a pickle file (`car_model.pkl`). This pickle file contains the serialized version of the trained model.

3. **App.py Integration**: In the `app.py` file (or any other file where you want to deploy the model), load the trained model from the pickle file (`car_model.pkl`) using the `pickle.load()` function. Ensure that the pickle file is located in the same directory as the `app.py` file.

## Repository Contents

In this repository, you'll find:

- `car_price.ipynb`: Jupyter Notebook containing the Python code for data preprocessing, model training, and pickle model export.
  
- `Cardetails.csv`: Dataset containing car details and selling prices.
  
- `car_model.pkl`: Pickle file containing the trained machine learning model for car price prediction.
  
- `app.py`: Python script for deploying the trained model into a Streamlit web application.

## Instructions

To run the car price prediction model:

1. Clone this repository to your local machine.

2. Ensure you have Python and necessary libraries (such as pandas, numpy, scikit-learn, and streamlit) installed on your system.

3. Execute the Jupyter Notebook  to train the model and export it as a pickle file.

4. Run the `app.py` file using Python:

   ```bash
   streamlit run app.py
   ```

5. Access the web application in your browser and use it to predict car prices based on the input features.
