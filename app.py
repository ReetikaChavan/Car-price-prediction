import pandas as pd  # Importing pandas library for data manipulation
import numpy as np   # Importing numpy library for numerical computations
import pickle as pk  # Importing pickle library for loading the trained machine learning model
import streamlit as st  # Importing streamlit library for creating the web application

model = pk.load(open('car_model.pkl','rb'))  # Loading the trained machine learning model from the pickle file

st.header('Car Price Prediction')  # Displaying a header for the web application

cars_data = pd.read_csv('Cardetails.csv')  # Reading the car details dataset into a pandas DataFrame

# Function to extract the brand name from the car name
def get_brand_name(car_name):
    car_name = car_name.split(' ')[0]  # Splitting the car name by space and extracting the first part
    return car_name.strip()  # Removing leading and trailing whitespaces from the extracted brand name

# Applying the 'get_brand_name' function to extract the brand name from the 'name' column of the DataFrame
cars_data['name'] = cars_data['name'].apply(get_brand_name)

# Creating select box widget for selecting the car brand from the unique values of the 'name' column
name = st.selectbox('Select Car Brand', cars_data['name'].unique())

# Creating a slider widget for selecting the car manufactured year
year = st.slider('Car Manufactured Year', 1994,2024)

# Creating a slider widget for selecting the number of kilometers driven by the car
km_driven = st.slider('No of kms Driven', 11,200000)

# Creating select box widget for selecting the fuel type from the unique values of the 'fuel' column
fuel = st.selectbox('Fuel type', cars_data['fuel'].unique())

# Creating select box widget for selecting the seller type from the unique values of the 'seller_type' column
seller_type = st.selectbox('Seller  type', cars_data['seller_type'].unique())

# Creating select box widget for selecting the transmission type from the unique values of the 'transmission' column
transmission = st.selectbox('Transmission type', cars_data['transmission'].unique())

# Creating select box widget for selecting the owner type from the unique values of the 'owner' column
owner = st.selectbox('Seller  type', cars_data['owner'].unique())

# Creating a slider widget for selecting the car mileage
mileage = st.slider('Car Mileage', 10,40)

# Creating a slider widget for selecting the car engine CC
engine = st.slider('Engine CC', 700,5000)

# Creating a slider widget for selecting the maximum power of the car
max_power = st.slider('Max Power', 0,200)

# Creating a slider widget for selecting the number of seats in the car
seats = st.slider('No of Seats', 5,10)

# Handling button click event for prediction
if st.button("Predict"):
    # Creating a pandas DataFrame with the input data
    input_data_model = pd.DataFrame(
    [[name,year,km_driven,fuel,seller_type,transmission,owner,mileage,engine,max_power,seats]],
    columns=['name','year','km_driven','fuel','seller_type','transmission','owner','mileage','engine','max_power','seats'])
    
    # Encoding categorical variables to numerical values for model prediction
    input_data_model['owner'].replace(['First Owner', 'Second Owner', 'Third Owner',
       'Fourth & Above Owner', 'Test Drive Car'],
                           [1,2,3,4,5], inplace=True)
    input_data_model['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'],[1,2,3,4], inplace=True)
    input_data_model['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'],[1,2,3], inplace=True)
    input_data_model['transmission'].replace(['Manual', 'Automatic'],[1,2], inplace=True)
    input_data_model['name'].replace(['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
       'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
       'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
       'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
       'Ambassador', 'Ashok', 'Isuzu', 'Opel'],
                          [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
                          ,inplace=True)

    # Making predictions using the loaded machine learning model
    car_price = model.predict(input_data_model)

    # Displaying the predicted car price
    st.markdown('Car Price is going to be '+ str(car_price[0]))
